"""
Name : Roey Firan
Program name : Data_Base
Date : 30/11/2022
Description: takes care of the threading and processing (syncing)
"""
import multiprocessing
import threading


class Synchronization:
    def __init__(self, data_base, mode):
        """
        init function
        :param data_base: database, object
        :param mode: bool
        """
        super().__init__()
        self.mode = mode
        self.dictionary = data_base
        if self.mode:
            self.lock = threading.Lock()
            self.semaphore = threading.Semaphore(10)
        else:
            self.lock = multiprocessing.Lock()
            self.semaphore = multiprocessing.Semaphore(10)

    def set_value(self, key, value):
        """
        set value function
        :param key: key in dictionary
        :param value: val in dictionary
        :return: result
        """
        self.lock.acquire()
        for i in range(10):
            self.semaphore.acquire()
        result = self.dictionary.set_value(key, value)
        for i in range(10):
            self.semaphore.release()
        self.lock.release()
        return result

    def get_value(self, key):
        """
        get value function.
        :param key: int
        :return: value, int
        """
        self.semaphore.acquire()
        value = self.dictionary.get_value(key)
        self.semaphore.release()
        return value

    def delete_value(self, key):
        """
        deletes the value of the given key
        :param key: int
        :return: value, int
        """
        self.lock.acquire()
        value = self.get_value(key)
        self.set_value(key, None)
        self.lock.release()
        return value

    def __str__(self):
        """
        print function
        :return: str
        """
        return f'The dictionary: {self.dictionary}'

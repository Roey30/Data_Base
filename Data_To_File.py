"""
Name : Roey Firan
Program name : Data_Base
Date : 30/11/2022
Description: Data to file class - takes the database and transfer it to a file
"""

import os
from pickle import *
from DataBase import *


class Data_to_file(Database):
    def __init__(self, filename):
        super().__init__()
        self.file = filename
        if not os.path.isfile(self.file):
            file = open(self.file, "wb")
            dump(self.dictionary, file)
            file.close()

    def write_file(self):
        if os.path.isfile(self.file):
            file = open(self.file, "wb")
            if file.writable() and self.dictionary is not None:
                dump(self.dictionary, file)
            file.close()

    def read_file(self):
        if os.path.isfile(self.file):
            file = open(self.file, "rb")
            if file.readable():
                self.dictionary = load(file)
                file.close()
                return self.dictionary
            file.close()

    def set_value(self, key, val):
        """
        set value function
        :param key: int
        :param val: int
        :return: result, int
        """
        self.read_file()
        result = super().set_value(key, val)
        self.write_file()
        return result

    def get_value(self, key):
        """
        get value function.
        :param key: int
        :return: val, int
        """
        self.read_file()
        return super().get_value(key)

    def delete_value(self, key):
        """
        deletes the value of the given key
        :param key: int
        :return: val, int
        """
        self.read_file()
        result = super().delete_value(key)
        self.write_file()
        return result

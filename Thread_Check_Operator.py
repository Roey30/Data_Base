"""
Name : Roey Firan
Program name : Data_Base
Date : 30/11/2022
Description: Uses to sync the data_base using threads
"""
from synchronization import Synchronization
from Data_To_File import Data_to_file
import threading
import logging

FILE_NAME = "Threads_Check.bin"


def main():
    """
    calls the reader and the writer methods.
     using threading.
     :return: None
     """
    logging.debug("Begins checking for process:")
    list_threads = Data_to_file(FILE_NAME)
    sync = Synchronization(list_threads, False)
    logging.info("checking simple writing")
    write_check = threading.Thread(target=check_write_function, args=(sync,))
    write_check.start()
    write_check.join()
    logging.info("The check has been completed")
    logging.info("checking simple reading")
    read_check = threading.Thread(target=check_read_function, args=(sync,))
    read_check.start()
    read_check.join()
    logging.info("The check has been completed")
    logging.info("checking reading while writing")
    read_check = threading.Thread(target=check_read_function, args=(sync,))
    write_check = threading.Thread(target=check_write_function, args=(sync,))
    read_check.start()
    write_check.start()
    read_check.join()
    write_check.join()
    logging.info("The check has been completed")
    logging.info("checking writing while reading")
    write_check = threading.Thread(target=check_write_function, args=(sync,))
    read_check = threading.Thread(target=check_read_function, args=(sync,))
    write_check.start()
    read_check.start()
    write_check.join()
    read_check.join()
    logging.info("The check has been completed")
    logging.info("checking multiple reading")
    threads = []
    for i in range(10):
        read_check = threading.Thread(target=check_read_function, args=(sync,))
        read_check.start()
        threads.append(read_check)
    for i in threads:
        i.join()
    logging.info("The check has been completed")
    threads = []
    for i in range(20):
        read_check = threading.Thread(target=check_read_function, args=(sync,))
        read_check.start()
        threads.append(read_check)
    for i in range(10):
        write_check = threading.Thread(target=check_write_function, args=(sync,))
        write_check.start()
        threads.append(write_check)
    for i in threads:
        i.join()
    logging.info("The check has been completed")
    logging.info("checking if the values has stayed correct")
    read_check = threading.Thread(target=check_read_function, args=(sync,))
    read_check.start()
    read_check.join()
    logging.info("The check has been completed")


def check_write_function(list_thread):
    logging.debug('begins check writing')
    for number in range(1000):
        assert list_thread.set_value(number, number)


def check_read_function(list_thread):
    logging.debug('begins check writing')
    for number in range(1000):
        assert (number == list_thread.get_value(number))


if __name__ == '__main__':
    logging.basicConfig(filename="CheckThread.log", filemode="a", level=logging.DEBUG)
    main()

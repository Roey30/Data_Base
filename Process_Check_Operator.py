"""
Name : Roey Firan
Program name : Data_Base
Date : 30/11/2022
Description: Uses to sync the data_base using processing
"""
from multiprocessing import Process
from synchronization import Synchronization
from Data_To_File import Data_to_file
import logging

FILE_NAME = "Process_Check.bin"


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
    write_check = Process(target=check_write_function, args=(sync,))
    write_check.start()
    write_check.join()
    logging.info("The check has been completed")
    logging.info("checking simple reading")
    read_check = Process(target=check_read_function, args=(sync,))
    read_check.start()
    read_check.join()
    logging.info("The check has been completed")
    logging.info("checking reading while writing")
    read_check = Process(target=check_read_function, args=(sync,))
    write_check = Process(target=check_write_function, args=(sync,))
    read_check.start()
    write_check.start()
    read_check.join()
    write_check.join()
    logging.info("The check has been completed")
    logging.info("checking writing while reading")
    write_check = Process(target=check_write_function, args=(sync,))
    read_check = Process(target=check_read_function, args=(sync,))
    write_check.start()
    read_check.start()
    write_check.join()
    read_check.join()
    logging.info("The check has been completed")
    logging.info("checking multiple reading")
    processes = []
    for i in range(10):
        read_check = Process(target=check_read_function, args=(sync,))
        read_check.start()
        processes.append(read_check)
    for i in processes:
        i.join()
    logging.info("The check has been completed")
    processes = []
    for i in range(20):
        read_check = Process(target=check_read_function, args=(sync,))
        read_check.start()
        processes.append(read_check)
    for i in range(10):
        write_check = Process(target=check_write_function, args=(sync,))
        write_check.start()
        processes.append(write_check)
    for i in processes:
        i.join()
    logging.info("The check has been completed")
    logging.info("checking if the values has stayed correct")
    read_check = Process(target=check_read_function, args=(sync,))
    read_check.start()
    read_check.join()
    logging.info("The check has been completed")


def check_write_function(list_process):
    logging.debug('begins check writing')
    for number in range(1000):
        assert list_process.set_value(number, number)


def check_read_function(list_process):
    logging.debug('begins check writing')
    for number in range(1000):
        assert (number == list_process.get_value(number))


if __name__ == '__main__':
    logging.basicConfig(filename="CheckProcess.log", filemode="a", level=logging.DEBUG)
    main()

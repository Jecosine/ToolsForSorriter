import logging

from .tools import check_exist_file, unpack_line


class Reader:
    def __init__(self, path, line_format=None):
        """
        Initialize reader
        Args:
            path(str): path to data file relative to `main.py`
            line_format(tuple): tuple contains corresponding element type. e.g. data: `1 2 3.1` <=> `(int, int, float)`
        """
        self.line_format = line_format
        self.path = path
        if not check_exist_file(path):
            logging.log(logging.ERROR, f'[ERROR] File not exists: {path}')
            exit(1)
        self.data_file = open(path, 'r')
        self.process_line = None  # need to be defined by decorator before calling read_file

    def read_file(self):
        """
        Read data line by line
        Returns:
            None
        """
        # process start ( ´▽｀)
        line = self.data_file.readline()
        while line:
            self.process_line(line)
            line = self.data_file.readline()

    def line_process(self, func):
        def wrapper(line):
            els = unpack_line(line, self.line_format)
            if els:
                func(els)

        self.process_line = wrapper
        return wrapper

    def line_process_without_format(self, func):
        def wrapper(line):
            if line:
                func(line)

        self.process_line = wrapper
        return wrapper

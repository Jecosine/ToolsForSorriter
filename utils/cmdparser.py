import argparse
import json
from typing import Any


class ArgParser:
    """
    Use config file to define a arg parser
    """

    def __init__(self, description: str):
        """
        Init parser with configuration
        Args:
            description:
        """
        self.__parser = argparse.ArgumentParser(description)
        self.args = None
        self.args_dict = {}

    def get_parsed_dict(self):
        return self.args.__dict__

    def parse(self):
        self.args = self.__parser.parse_args()
        print(self.args_dict, self.args.__dict__)
        for k, v in self.args_dict.items():
            self.args_dict[k](self.args.__dict__.get(k))

    def on(self, short_name: str, long_name: str, help_str: str = '', default: Any = None, data_type: type = None):
        """
        Define a decorator to map the action with args
        Args:
            short_name:
            long_name:
            help_str:
            default:
            data_type:

        Returns: Function

        """
        self.__parser.add_argument(short_name, long_name, type=data_type, default=default, help=help_str)

        def fun_wrapper(func):
            self.args_dict[long_name[2:]] = func

        return fun_wrapper

# if __name__ == '__main__':
# a = ArgParser('New parser')
#
#
# @a.on('-a', '--add', 'add number', data_type=int)
# def foo(x):
#     print(1 + x)
#
#
# a.parse()

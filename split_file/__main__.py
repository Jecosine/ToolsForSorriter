import os
import argparse
from typing import Any

from utils import Reader, check_exist_file, ArgParser, unpack_line

a = ArgParser('Split specified file')
dst_path = ''
src_path = ''


@a.on('-d', '--dst_dir', default='./dst/section1')
def get_dst_dir(path):
    global dst_path
    if not check_exist_file(path):
        raise Exception(f'File or directory {path} not exist')
    else:
        dst_path = path


@a.on('-s', '--src_dir', default='./data/test.dat')
def get_src_dir(path):
    global src_path
    if not check_exist_file(path):
        raise Exception(f'File or directory {path} not exist')
    else:
        src_path = path


# parse cmd argument
a.parse()
# initialize reader
reader = Reader(src_path)
formats = [
    {
        'types': (float, float, float, float),
        'map': ('z', 'x', 'd', '-', '-')
    },
    {
        'types': (str, str, float, str),
        'map': ('-', '-', 't', '-')
    }
]

file_cursor: Any = None


@reader.line_process_without_format
def split_file(line):
    global file_cursor
    if line[0] == 'T':
        t = '%.7f' % unpack_line(line, formats[1]['types'])[2]
        file_name = t.replace('.', '-')
        if file_cursor is not None:
            file_cursor.close()
        file_cursor = open(os.path.join(dst_path, f'{file_name}.dat'), 'w')
    else:
        file_cursor.write(line)


reader.read_file()
if file_cursor is not None:
    file_cursor.close()

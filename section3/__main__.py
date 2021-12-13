import os
import argparse
from typing import Any

import numpy as np

from utils import Reader, check_exist_file, ArgParser, unpack_line

a = ArgParser('Get z - density data')
dst_path = ''
src_path = ''


@a.on('-d', '--dst_path', default='./dst/section2/dst.dat')
def get_dst_dir(path):
    global dst_path
    dst_path = path


@a.on('-s', '--src_path', default='./dst/section1')
def get_src_dir(path):
    global src_path
    if not check_exist_file(path):
        raise Exception(f'File or directory {path} not exist')
    else:
        src_path = path


# parse cmd argument
a.parse()
time_mat = np.loadtxt(os.path.join(dst_path, 'step2/dst.dat'), delimiter=' ', skiprows=1)
time_mat = np.concatenate((np.array([[0,] + [float(i) / 4.0 for i in range(200)],], dtype=np.float64), time_mat))
time_mat.transpose()
np.savetxt(os.path.join(dst_path, 'step3/dst.dat'), time_mat.transpose(), delimiter=' ')
import os
import argparse
from typing import Any

import numpy as np

from utils import Reader, check_exist_file, ArgParser, unpack_line

a = ArgParser('Get z - density data')
dst_path = ''
src_path = ''


@a.on('-d', '--dst_path', default='./dst/')
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


def calc(X: np.core._multiarray_umath.ndarray):
    p = np.power(X.mean(), 2)
    if p == 0:
        return 0
    t = np.power(X, 2).mean() / p
    if t < 1:
        return 0
    else:
        return np.sqrt(t - 1)


# parse cmd argument
a.parse()
time_mat = []
# preprocess: grouped data by z-index
time_array = sorted(os.listdir(src_path), key=lambda x: x)
# Add header line
header = ' '.join([str(float(i) / 4.0) for i in range(200)])
for ts in time_array:
    time_float = float(os.path.splitext(ts)[0].replace('-', '.'))
    ts_data = np.genfromtxt(os.path.join(src_path, ts))
    # assert the shape is (12000, 6)
    assert ts_data.shape == (12000, 6)
    # z_group is a list where the element(array) shares the same `z`
    z_group = np.split(ts_data, 200, axis=0)
    # time rows
    time_rows = [time_float] + [
        calc(z_stack[:, 2]) for z_stack in z_group
    ]
    time_mat.append(time_rows)

time_mat = np.array(time_mat)
np.savetxt(os.path.join(dst_path, 'step5/dst.dat'), time_mat, delimiter=' ', header=header)

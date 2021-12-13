import math
import numpy as np

from utils import Reader

if __name__ == '__main__':
    path = 'data/density.dat'  # data path to rewrite
    line_format = (float, float, float, float)
    reader = Reader(path, line_format)
    # store result in data_dict:
    #  {
    #    [value in column C] : [length, avg_of_square, square_of_avg]
    #  }
    data_dict = {}


    # define line process function
    @reader.line_process
    def custom_processor(els):
        if not data_dict.get(els[2]):
            data_dict[els[2]] = [0, 0, 0, 0]
        data_dict[els[2]][0] += 1
        data_dict[els[2]][1] += els[3] ** 2
        data_dict[els[2]][2] += els[3]


    # start reading
    reader.read_file()

    # calculate average
    for i in range(0, 5000, 25):
        length = data_dict[i / 100][0]
        data_dict[i / 100][1] /= length
        data_dict[i / 100][2] /= length

    # output file (if needed, just for example)
    with open('output.dat', 'w') as f:
        for i in range(0, 5000, 25):
            k = i / 100
            data_dict[k][2] **= 2
            data_dict[k][3] = np.sqrt(data_dict[k][1] / data_dict[k][2] - 1) if data_dict[k][2] != 0 else 0
            # format: "`column C` `total length` `avg of square` `square of avg`"
            f.write('{} {} {} {} {}\n'.format(k, *data_dict[k]))

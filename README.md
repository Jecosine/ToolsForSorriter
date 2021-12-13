# Utils for Sorriter

## Description

`./dst` serves for storing the target data files.
`./data` contains the origin data file `dens_zx.dat`, where you must ensure the file's existed before you run following
commands. You should generate data files in step1 by yourself, since it takes too long to compress overwhelm data
segments...

## Section 1 File splitting

Make sure you run commands under the root path of this project.

```shell
$ pwd
/path/to/sorriter
```

Usage:

```shell
$ python -m split_file -h
usage: Split specified file [-h] [-d DST_DIR] [-s SRC_DIR]

optional arguments:
  -h, --help            show this help message and exit
  -d DST_DIR, --dst_dir DST_DIR
  -s SRC_DIR, --src_dir SRC_DIR
```

Example:

```shell
$ python -m split_file -s ./data/dens_zx.dat -d ./dst/step1
```

## Section 2 & 3

**Run `section2` first**

```shell
python -m section2 -s ./dst/section1 -d ./dst/
```

File header (A `#` is included as the first character in the header)

```
# 0 0.25 ...
```

Section 3 is just the transposed-matrix of section 2

```shell
python -m section3 -s ./dst/section1 -d ./dst/
```

File header, 0 is used to pad the first col's header  (the numbers may be kind of weird due to the accuracy problem...)

```
0.000000000000000000e+00 1.999999999999999909e-07 1.000199999999999917e-03 ...
```

## Section 4 & 5

**Run `section5` first**

```shell
python -m section5 -s ./dst/section1 -d ./dst/
```

File header (A `#` is included as the first character in the header)

```
# 0 0.25 ...
```

Section 4 is just the transposed-matrix of section 5

```shell
python -m section4 -s ./dst/section1 -d ./dst/
```

File header, 0 is used to pad the first col's header  (the numbers may be kind of weird due to the accuracy problem...)

```
0.000000000000000000e+00 1.999999999999999909e-07 1.000199999999999917e-03 ...
```
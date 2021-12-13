import logging
import os


def unpack_line(s, line_format):
    s = s.strip()
    if not s:
        return None
    sl = s.split(' ')
    try:
        assert len(line_format) == len(sl)
    except AssertionError:
        logging.log(logging.ERROR, '[ERROR] Elements amount does not consist with given format')
        exit(1)
    return [line_format[i](e) for i, e in enumerate(sl)]


def check_exist_file(path, create_if_not_exist=False):
    if os.path.exists(path):
        return True
    elif create_if_not_exist:
        try:
            with open(path, 'w') as f:
                logging.log(logging.INFO, f'[INFO] File created: {path}')
        except Exception as e:
            logging.log(logging.ERROR, f'[ERROR] Cannot create file {path}:\n{str(e)}')
    else:
        return False

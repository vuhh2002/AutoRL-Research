import os
import pathlib
from datetime import datetime


class Handler():

    def __init__(self):
        pass

    def time_stamp(self) -> str:
        return datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S.%f')[:-4]

    def save_mkdir(self, dir):
        try:
            os.makedirs(dir, exist_ok=True)
        except:
            pass

    def counting_name(self, dir, file_name, suffix=False):
        dir = pathlib.Path(dir)
        counter = 0
        split_file_name = file_name.split('.')
        if suffix:
            counting_file_name = '.'.join(split_file_name[:-1]) + f"-{counter}." + split_file_name[-1]
        else:
            counting_file_name = file_name + f"-{counter}"

        while os.path.isfile(dir / counting_file_name) or os.path.isdir(dir / counting_file_name):
            if suffix:
                counting_file_name = '.'.join(split_file_name[:-1]) + f"-{counter}." + split_file_name[-1]
            else:
                counting_file_name = file_name + f"-{counter}"
            counter += 1

        return counting_file_name

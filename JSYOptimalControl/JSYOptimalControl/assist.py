"""
Author:YCY
Time:
Descrption:
"""

import time
import os
import sys


class Log(object):
    def __init__(self, input_info):
        self._input_info = input_info

    def write_log(input_info):
        # Get logFile Path
        current_path = sys.path[0]
        result_path = ""
        if os.path.isdir(current_path):
            result_path = current_path
        elif os.path.isfile(current_path):
            result_path = current_path

        log_file_path = result_path + "\log" + time.strftime('\%Y-%m-%d', time.localtime(time.time())) + ".txt"
        try:
            f = open(log_file_path, 'w')
            f.write(input_info + '\n')
            f.close()
        except Exception as e:
            print(e)





# we are going to add the chromedriver bin directory to PATH

import sys
import os

full_file_path = os.path.realpath(__file__)

# get current directory for this file, environment.py
file_dirname = os.path.dirname(full_file_path)
# print(file_dirname)
# ..../features

parent_dirname = os.path.dirname(file_dirname)
# print(parent_dirname)
# sys.path.insert(0,'/path/to/mod_directory')

path_to_bin = os.path.join(parent_dirname, 'bin')
print(path_to_bin.__class__.__name__)

# sys.path.insert(0, path_to_bin)
# print(sys.path)

def bin_path():
    full_file_path = os.path.realpath(__file__)
    file_dirname = os.path.dirname(full_file_path)
    parent_dirname = os.path.dirname(file_dirname)
    return os.path.join(parent_dirname, 'bin', 'chromedriver')


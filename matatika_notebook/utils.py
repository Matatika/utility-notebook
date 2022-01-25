"""Module containing utility functions"""

import os


def get_file_name_with_ext(path):
    """Return file name with extension"""
    _, tail = os.path.split(path)

    return tail


def get_file_name_no_ext(path):
    """Return file name without extension"""
    _, tail = os.path.split(path)
    (nb_name, _) = os.path.splitext(tail)

    return nb_name


def get_file_extension(path):
    """Return file extension"""
    _, tail = os.path.split(path)
    (_, ext) = os.path.splitext(tail)

    return ext


def get_list_of_paths(path):
    """Return list of paths for file or all files in a directory"""
    path_list = []
    if os.path.isfile(path):
        path_list.append(path)
    elif os.path.isdir(path):
        abs_path = os.path.abspath(path)
        for file_name in os.listdir(abs_path):
            path_list.append(path + "/" + file_name)
    return path_list

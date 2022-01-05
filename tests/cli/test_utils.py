"""Module containing test utility functions and data"""

import os

pdf_file_list = [
    "test_notebook_one.pdf",
    "test_notebook_two.pdf",
    "test_notebook_three.pdf",
]


def clean_up_converted_test_files(test_files_path):
    """Cleans up converted pdf and markdown files in the test_files dir"""
    dir_list = os.listdir(test_files_path)
    for file in dir_list:
        file_path = test_files_path.joinpath(file)
        if os.path.isdir(file_path):
            clean_up_converted_test_files(file_path)
        else:
            if file.endswith(".pdf") or file.endswith(".md"):
                os.remove(file_path)

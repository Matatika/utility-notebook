import os


def clean_up_converted_test_files(test_files_path):

    dir_list = os.listdir(test_files_path)
    for file in dir_list:
        file_path = test_files_path.joinpath(file)
        if os.path.isdir(file_path):
            clean_up_converted_test_files(file_path)
        else:
            if file.endswith(".pdf") or file.endswith(".md"):
                os.remove(file_path)

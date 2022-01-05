"""Module for executing jupyter notebooks"""
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import click

from .utils import get_file_extension, get_file_name_with_ext


def run_notebook(path_list):
    """Execute all jupyter notebooks on given paths"""
    for path in path_list:
        nb_filename_with_ext = get_file_name_with_ext(path)
        file_extension = get_file_extension(path)

        if file_extension == ".ipynb":

            click.secho(f"Executing {nb_filename_with_ext}...", fg="white")

            with open(path, "r+", encoding="utf-8") as nb_file:
                notebook = nbformat.read(nb_file, as_version=4)
                execute_preprocessor = ExecutePreprocessor()
                execute_preprocessor.preprocess(notebook)

                nb_file.seek(0)
                nbformat.write(notebook, nb_file)
                nb_file.truncate()

            click.secho(f"Ran file: {nb_filename_with_ext}", fg="green")
        else:
            click.secho(
                f"Skipped file: {nb_filename_with_ext}. Incorrect file type",
                fg="yellow",
            )

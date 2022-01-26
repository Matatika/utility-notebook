"""Module for converting jupyter notebooks"""

import os

import click
from nbconvert import PDFExporter


from matatika_notebook.utils import (
    get_file_name_no_ext,
    get_file_name_with_ext,
    get_file_extension,
)

from matatika_notebook.pdf_format_settings import pdf_config_setup


def convert_notebook(path_list, notebook_format, config):
    """Convert all notebooks in the path list"""
    for path in path_list:
        nb_filename_with_ext = get_file_name_with_ext(path)
        file_extension = get_file_extension(path)
        if file_extension == ".ipynb":
            if notebook_format == "pdf":
                convert_to_pdf(path, config)
        else:
            click.secho(
                f"Skipped file: {nb_filename_with_ext}. Incorrect file type",
                fg="yellow",
            )


def convert_config(config, notebook_format):
    """Handles the converted files config"""
    if notebook_format == "pdf":
        pdf_config = pdf_config_setup(config)
        return PDFExporter(config=pdf_config)
    return None


def save_converted_notebook(path, body, notebook_format):
    """Saves converted notebook"""
    nb_filename_no_ext = get_file_name_no_ext(path)

    click.secho(
        f"Saving notebook as {nb_filename_no_ext}.{notebook_format}...",
        fg="white",
    )

    filepath, _ = os.path.split(path)

    filepath = filepath + "/" + nb_filename_no_ext + "." + notebook_format

    with open(filepath, "wb") as file:
        file.write(body)


def convert_to_pdf(path, config):
    """Handles converting notebook to pdf"""
    nb_filename_with_ext = get_file_name_with_ext(path)

    click.secho(
        f"Converting {nb_filename_with_ext} to PDF...",
        fg="white",
    )

    pdf_exporter = convert_config(config, "pdf")

    (body, _) = pdf_exporter.from_filename(path)

    save_converted_notebook(path, body, "pdf")

    click.secho(f"Converted file: {nb_filename_with_ext} to .pdf", fg="green")

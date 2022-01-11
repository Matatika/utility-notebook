# pylint:disable=duplicate-code

"""CLI 'convert' command"""

import sys
import click
import os

from notebook.utils import get_list_of_paths
from notebook.notebook_converter import convert_notebook
from .root import notebook


@notebook.command(
    "convert", short_help="Convert a Jupyter notebook, or all notebooks in a directory"
)
@click.argument(
    "path", type=click.Path(exists=True), default=os.getenv("NOTEBOOK_PATH")
)
@click.option(
    "--format",
    "-f",
    "format_",
    type=click.STRING,
    help="What format you want to convert your notebook into. Supported formats: PDF",
    default=os.getenv("NOTEBOOK_FORMAT"),
)
def convert(path, format_):
    """Convert a notebook or all notebooks in a directory"""

    if format_:
        path_list = get_list_of_paths(path)

        convert_notebook(path_list, format_)
    else:
        click.secho("No format provided for conversion.", fg="red")
        sys.exit(2)

# pylint:disable=duplicate-code, unused-argument

"""CLI 'convert' command"""

import sys
import click

from notebook.utils import get_list_of_paths
from notebook.notebook_converter import convert_notebook
from .root import notebook


@notebook.command(
    "convert", short_help="Convert a Jupyter notebook, or all notebooks in a directory"
)
@click.pass_context
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--format",
    "-f",
    type=click.STRING,
    help="What format you want to convert your notebook into. Supported formats: PDF",
)
def convert(ctx, path, notebook_format):
    """Convert a notebook or all notebooks in a directory"""

    if notebook_format:
        path_list = get_list_of_paths(path)

        convert_notebook(path_list, notebook_format)
    else:
        click.secho("No format provided for conversion.", fg="red")
        sys.exit(2)

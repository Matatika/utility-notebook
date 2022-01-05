# pylint:disable=duplicate-code, unused-argument

"""CLI 'run' command"""

import click

from notebook.notebook_converter import convert_notebook
from notebook.notebook_runner import run_notebook
from notebook.utils import get_list_of_paths
from .root import notebook


@notebook.command("run", short_help="Run the notebook")
@click.pass_context
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--format",
    "-f",
    type=click.STRING,
    help="What format you want to convert your notebook into. Supported formats: PDF",
)
def run(ctx, path, notebook_format):
    """Run a notebook or all notebooks in a directory"""

    path_list = get_list_of_paths(path)

    run_notebook(path_list)

    if notebook_format:
        convert_notebook(path_list, notebook_format)

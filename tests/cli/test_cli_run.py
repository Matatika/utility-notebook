import unittest
import os
from pathlib import Path
from click.testing import CliRunner
from notebook.cli.commands.root import notebook
from tests.cli.test_utils import clean_up_converted_test_files


class TestRun(unittest.TestCase):
    def setUp(self):
        self.package_dir = Path(__file__).parent.parent.absolute()
        self.notebook_path = self.package_dir.joinpath("test_files/test_notebook.ipynb")
        self.notebook_dir_path = self.package_dir.joinpath("test_files/notebook_dir/")
        self.test_files_path = self.package_dir.joinpath("test_files/")

        self.runner = CliRunner()

    def tearDown(self):
        clean_up_converted_test_files(self.test_files_path)

    def test_run_with_no_file_path(self):
        # Test the run command without a file path
        result = self.runner.invoke(notebook, ["run"])
        print(result.output)
        self.assertIn("Error: Missing argument 'PATH'", result.output)
        self.assertIs(result.exit_code, 2)

    def test_run_with_incorrect_file_type(self):
        # Test the run command with an incorrect file type
        self.text_file_path = self.test_files_path.joinpath("text_file.txt")
        result = self.runner.invoke(notebook, ["run", str(self.text_file_path)])
        print(result.output)
        self.assertIn("Skipped file:", result.output)

    def test_run(self):
        # Test running a notebook
        result = self.runner.invoke(notebook, ["run", str(self.notebook_path)])
        self.assertIn("Ran file: ", result.output)
        self.assertIs(result.exit_code, 0)

    def test_run_all_notebooks_in_a_dir(self):
        # Test running all notebooks in a dir
        result = self.runner.invoke(notebook, ["run", str(self.notebook_dir_path)])
        self.assertIn("test_notebook_one.ipynb", result.output)
        self.assertIn("test_notebook_two.ipynb", result.output)
        self.assertIn("test_notebook_three.ipynb", result.output)
        self.assertIs(result.exit_code, 0)

    def test_run_and_convert(self):
        # Test running and then converting a notebook
        result = self.runner.invoke(
            notebook, ["run", str(self.notebook_path), "-f", "pdf"]
        )
        self.assertIs(result.exit_code, 0)
        self.assertIn("Ran file: ", result.output)

        self.assertIn("Converted file: ", result.output)
        pdf_path = self.test_files_path.joinpath("test_notebook.pdf")
        self.assertTrue(pdf_path.is_file())

    def test_run_and_convert_notebooks_in_a_dir(self):
        # Test running and then converting all notebook in target dir
        result = self.runner.invoke(
            notebook, ["run", str(self.notebook_dir_path), "-f", "pdf"]
        )
        self.assertIs(result.exit_code, 0)
        self.assertIn("test_notebook_one.ipynb", result.output)
        self.assertIn("test_notebook_two.ipynb", result.output)
        self.assertIn("test_notebook_three.ipynb", result.output)

        self.assertIn("Converted file: ", result.output)
        self.assertIn("test_notebook_one.ipynb", result.output)
        self.assertIn("test_notebook_two.ipynb", result.output)
        self.assertIn("test_notebook_three.ipynb", result.output)

        pdf_file_list = [
            "test_notebook_one.pdf",
            "test_notebook_two.pdf",
            "test_notebook_three.pdf",
        ]

        for file in pdf_file_list:
            pdf_path = self.notebook_dir_path.joinpath(file)
            self.assertTrue(pdf_path.is_file())

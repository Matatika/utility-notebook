"""Unittest module for notebook convert"""

import unittest
from pathlib import Path
from click.testing import CliRunner
from tests.cli.test_utils import clean_up_converted_test_files, pdf_file_list
from matatika_notebook.cli.commands.root import notebook


class TestConvert(unittest.TestCase):
    """Unittest class for notebook convert"""

    def setUp(self):
        """notebook convert test setup"""
        self.runner = CliRunner()
        self.package_dir = Path(__file__).parent.parent.absolute()
        self.notebook_path = self.package_dir.joinpath("test_files/test_notebook.ipynb")
        self.notebook_dir_path = self.package_dir.joinpath("test_files/notebook_dir/")
        self.test_files_path = self.package_dir.joinpath("test_files/")

    def tearDown(self):
        """notebook convert test tear down"""
        clean_up_converted_test_files(self.test_files_path)

    def test_convert_with_no_file_path(self):
        """Test notebook convert with no file path provided"""
        result = self.runner.invoke(notebook, ["convert"])
        print(result.output)
        self.assertIn("Error: Missing argument 'PATH'", result.output)
        self.assertIs(result.exit_code, 2)

    def test_convert_with_no_format_flag(self):
        """Test notebook convert on single notebook with no format passed"""
        result = self.runner.invoke(notebook, ["convert", str(self.notebook_path)])
        self.assertIn("No format provided for conversion.", result.output)
        self.assertIs(result.exit_code, 2)

    def test_convert_with_format_flag_no_format(self):
        """Test notebook convert on single notebook with format flag but no format"""
        result = self.runner.invoke(
            notebook, ["convert", str(self.notebook_path), "-f"]
        )
        self.assertIn("Error: -f option requires an argument", result.output)
        self.assertIs(result.exit_code, 2)

    def test_convert_with_incorrect_file_type(self):
        """Test notebook convert with incorrect file type"""
        text_file_path = self.test_files_path.joinpath("text_file.txt")
        result = self.runner.invoke(
            notebook, ["convert", str(text_file_path), "-f", "pdf"]
        )
        print(result.output)
        self.assertIn("Skipped file:", result.output)

    def test_convert(self):
        """Test notebook convert on single notebook"""
        result = self.runner.invoke(
            notebook, ["convert", str(self.notebook_path), "-f", "pdf"]
        )
        self.assertIn("Converted file: ", result.output)
        self.assertIs(result.exit_code, 0)
        pdf_path = self.test_files_path.joinpath("test_notebook.pdf")
        self.assertTrue(pdf_path.is_file())

    def test_convert_notebooks_in_a_dir(self):
        """Test notebook convert on a directory of notebooks"""
        result = self.runner.invoke(
            notebook, ["convert", str(self.notebook_dir_path), "-f", "pdf"]
        )
        self.assertIn("Converted file: ", result.output)
        self.assertIn("test_notebook_one.ipynb", result.output)
        self.assertIn("test_notebook_two.ipynb", result.output)
        self.assertIn("test_notebook_three.ipynb", result.output)
        self.assertIs(result.exit_code, 0)

        for file in pdf_file_list:
            pdf_path = self.notebook_dir_path.joinpath(file)
            self.assertTrue(pdf_path.is_file())

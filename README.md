<a href="https://github.com/Matatika/notebook/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Matatika/notebook"></a>
# notebook
Meltano utility plugin for running and converting Jupyter notebooks.

# Usage

Can be pip installed and used as a python cli package.

Can be added to your Meltano project and used to run notebooks as reports.

## Supported Converting Formats

- PDF

# Commands

## Run

The run command will execute all cells in a notebook or a directory of notebooks and save the outputs.

### Single Notebook
`notebook run path/to/notebook.ipynb`

### Directory of Notebooks

This currently runs all notebooks in the top level of the selected directory.

`notebook run path/to/dir/of/notebooks`

### Single Notebook and Convert
`notebook run path/to/notebook.ipynb --format pdf`

### Directory of Notebooks and Convert
`notebook run path/to/dir/of/notebooks -f pdf`

---

## Convert

The convert command will convert your ipynb notebook to your selected format

### Single Notebook
`notebook convert path/to/notebook.ipynb -f pdf`

### Directory of Notebooks
`notebook convert path/to/dir/of/notebooks -f pdf`

---

## Install

The install command allows you to add requirements used in your notebooks to your python virtual environment or system python. 

You also have the option of using `pip install` INSIDE the notebook your plan on running and converting, though every time you run the notebook it will check all the python packages.

### Install a Requirements.txt
`notebook install path/to/requirements.txt`

---

## To-Do

- Add ability to add custom config for converting notebooks to pdf. 
(Currently its just a clean basic and you can do basic formatting within your notebook)

- Add ability to convert notebooks into .md files.

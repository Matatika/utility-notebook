from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="matatika-notebook",
    version="0.1.0",
    description="A Meltano utility plugin for running and converting Jupyter notebooks.",
    author="DanielPDWalker",
    url="https://www.matatika.com/",
    entry_points="""
        [console_scripts]
        notebook=matatika_notebook.cli.commands.root:notebook
    """,
    license="MIT",
    install_requires=required,
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
)

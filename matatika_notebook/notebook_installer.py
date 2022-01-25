"""Module for install python packages

Intended use is when you use notebook as a Meltano plugin and have to
install requirements to the venv that Meltano created on behalf of its plugins"""

import subprocess
import sys
from pathlib import Path


def install_requirements(requirements_path):
    """Install required packages from requirements.txt into current python enviroment"""
    requirements_path = str(Path(requirements_path).absolute())
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", requirements_path]
    )

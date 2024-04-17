import pathlib
import subprocess
from importlib.metadata import version
from invoke import task

# pylint: disable=missing-function-docstring,unused-argument

ROOT = pathlib.Path(__file__).parent.resolve().as_posix()
VERSION = version("sanity-tests")


@task
def tests(context):
    cmd = [
        "pytest",
        f"{ROOT}/tests",
    ]
    subprocess.run(" ".join(cmd), shell=True, check=False)

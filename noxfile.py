# Copyright 2022 simple-syslog authors
# All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Nox configuration file.

This Nox configuration utilizes nox-poetry for poetry support.
"""

from nox import options
from nox_poetry import session

# we by default only want to lint and test
# we don't want to modify with black
options.sessions = "lint", "mypy", "tests"
locations = "simple_syslog", "tests", "noxfile.py"


@session(python=["3.8", "3.9"])
def tests(session) -> None:
    """Run the test suite."""
    args = session.posargs or ["--cov"]
    session.install("coverage[toml]", ".")
    session.install("pytest", ".")
    session.install("pytest-cov", ".")
    session.install("pytest-mock", ".")
    session.install("cleo", ".")
    session.run("poetry", "install", external=True)
    session.run("pytest", *args, external=True)


@session(python=["3.8", "3.9"])
def lint(session):
    """Lint using Flake8."""
    args = session.posargs or locations
    session.install(
        "black",
        "darglint",
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-isort",
    )
    session.run("flake8", *args)


@session(python=["3.8", "3.9"])
def black(session):
    """Format using Black."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@session(python=["3.8", "3.9"])
def mypy(session):
    """Type Checking with mypy."""
    args = session.posargs or locations
    session.install("mypy", ".")
    session.run("mypy", *args)

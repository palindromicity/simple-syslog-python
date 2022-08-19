from nox import options
from nox_poetry import session

# we by default only want to lint and test
# we don't want to modify with black
options.sessions = "lint", "tests"
locations = "simple_syslog", "tests", "noxfile.py"


@session(python=["3.8", "3.9"])
def tests(session):
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
    args = session.posargs or locations
    session.install("black", "flake8", "flake8-black", "flake8-bugbear", "flake8-isort")
    session.run("flake8", *args)


@session(python=["3.8", "3.9"])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)

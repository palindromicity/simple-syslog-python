from nox_poetry import session

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
    session.install("flake8")
    session.run("flake8", *args)

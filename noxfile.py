from nox_poetry import session


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

# License: MIT
# Copyright © 2022 Frequenz Energy-as-a-Service GmbH

"""Project's noxfile.

For more information please see nox documentation:
https://nox.thea.codes/en/stable/
"""

from typing import List
import nox

DOCSTRING_DEPS = ["pydocstyle", "darglint", "tomli"]
FMT_DEPS = ["black"]
MYPY_DEPS = ["mypy", "pandas-stubs", "grpc-stubs"]


def _source_file_paths(session: nox.Session) -> List[str]:
    """Return the file paths to run the checks on.

    If positional arguments are present in the nox session, we use those as the
    file paths, and if not, we use all source files.

    Args:
        session: the nox session.

    Returns:
        list[str]: the file paths to run the checks on.
    """
    if session.posargs:
        return session.posargs
    return ["py", "pytests", "noxfile.py", "setup.py"]


@nox.session
def formatting(session: nox.Session, install_deps: bool = True) -> None:
    """Check code formatting with black.

    Args:
        session: the nox session.
        install_deps: True if dependencies should be installed.
    """
    if install_deps:
        session.install(*FMT_DEPS)

    session.run("black", "--check", "--diff", "pytests", "noxfile.py")


# This doesn't include the entire src/ folder because the instantaneous_peak_shaving actor
# is still not ready to be checked
@nox.session
def pylint(session: nox.Session) -> None:
    """Check code with pylint.

    Args:
        session: the nox session.
    """
    session.install(".", "pylint", "nox")
    session.run(
        "pylint",
        "noxfile.py",
        "setup.py",
    )


@nox.session
def docstrings(session: nox.Session, install_deps: bool = True) -> None:
    """Check docstring tone with pydocstyle and param descriptions with darglint.

    Args:
        session: the nox session.
        install_deps: True if dependencies should be installed.
    """
    if install_deps:
        session.install(*DOCSTRING_DEPS, "toml")

    session.run("pydocstyle", "noxfile.py", "setup.py")

    # Darglint checks that function argument and return values are documented.
    # This is needed only for the `src` dir, so we exclude the other top level
    # dirs that contain code, unless some paths were specified by argument, in
    # which case we use those untouched.
    session.run(
        "darglint",
        "-v2",  # for verbose error messages.
        "noxfile.py",
        "setup.py",
    )


@nox.session
def pytest(session: nox.Session) -> None:
    """Run pytest unit tests..

    Args:
        session: the nox session.
    """
    session.install("-r", "minimum-requirements-ci.txt")
    session.install("pytest", "pytest-asyncio")
    # install the package itself as editable, so that it is possible to do fast
    # local tests with `nox -R -e pytest`.
    session.install("-e", ".")
    session.run(
        "pytest",
        "-W=all",
        "--verbose",
    )

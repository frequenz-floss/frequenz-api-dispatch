"""Build script for the frequenz-api-dispatch python package.

Copyright © 2022 Frequenz Energy-as-a-Service GmbH.
"""

from distutils.command.build_py import build_py
import sys
import subprocess

import setuptools


class BuildProto(build_py):
    """Command class to build the Python protobuf files."""

    def run(self):
        """Build the Python protobuf files and run regular `build_py`."""
        subprocess.check_call(["./build-py-proto", sys.executable], shell=True)
        build_py.run(self)


setuptools.setup(
    name="frequenz-api-dispatch",
    author="Frequenz Energy-as-a-Service GmbH",
    description="Frequenz Dispatch API.",
    setup_requires=["setuptools_scm"],
    use_scm_version={"version_scheme": "post-release"},
    cmdclass={"build_py": BuildProto},
    install_requires=[
        "googleapis-common-protos >= 1.50.0, < 2",
        "grpcio >= 1.33.2, < 2",
    ],
    package_dir={"": "py"},
    packages=setuptools.find_namespace_packages(where="py"),
    python_requires=">= 3.7, < 4",
)

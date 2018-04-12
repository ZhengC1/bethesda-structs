# Copyright (c) 2018 Stephen Bunn (stephen@bunn.io)
# GPLv3 License <https://choosealicense.com/licenses/gpl-3.0/>

import os
import sys
import shutil
import setuptools

from bethesda_structs import __version__

INSTALL_REQUIRES = ["construct", "multidict", "attrs", "lz4"]
SETUP_REQUIRES = []
EXTRAS_REQUIRE = {
    "dev": [
        "ptpython",
        "flake8",
        "sphinx",
        "sphinx-autodoc-typehints",
        "sphinx-readable-theme",
        "pytest",
        "pytest-cov",
        "pytest-flake8",
        "pytest-sugar",
    ]
}


class UploadCommand(setuptools.Command):

    description = "Build and publish package"
    user_options = []

    @staticmethod
    def status(status):
        print(f"... {status}")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("removing previous builds")
            shutil.rmtree(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), "dist")
            )
        except FileNotFoundError:
            pass

        self.status("building distribution")
        os.system(f"{sys.executable} setup.py sdist")

        self.status("uploading distribution")
        os.system("twine upload dist/*")

        self.status("pushing git tags")
        os.system(f"git tag v{__version__.__version__}")
        os.system("git push --tags")

        sys.exit()


setuptools.setup(
    name=__version__.__name__,
    version=__version__.__version__,
    description=__version__.__description__,
    long_description=open("README.rst", "r").read(),
    url=__version__.__repo__,
    license=__version__.__license__,
    author=__vesrion__.__author__,
    author_email=__vesrion__.__contact__,
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    keywords=["bethesda", "filetype", "structures", "archive", "python36", "construct"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: English",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Disassemblers",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Utilities",
    ],
    cmdclass={"upload": UploadCommand},
)

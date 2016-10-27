# cpyImagingMSpec [![Documentation Status](https://readthedocs.org/projects/cpyimagingmspec/badge/?version=latest)](http://cpyimagingmspec.readthedocs.org/en/latest/?badge=latest)

Scoring imaging mass spectrometry images for multiple isotopes.

## Installation

Binary builds are provided for convenience, use `pip install cpyImagingMSpec`.
(You might have to run `pip install --upgrade pip` first, its version should be at least `8.1.1`.)

If it didn't work for you or you have security concerns, here's how to install the package from source:
- Install `cmake` and a recent version of `g++`, preferably 5.3
  - OS X: `brew install gcc5`
  - Ubuntu: install `gcc-5` package (on older versions from `ubuntu-toolchain-r` PPA)
  - Windows: install MSYS2 and the build toolchain (see `wheel_builders/README.md`)
- Call the appropriate script from `wheel_builders` folder with arguments 'ims-cpp ims_cffi'.

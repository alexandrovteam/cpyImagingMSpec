# cpyImagingMS [![Documentation Status](https://readthedocs.org/projects/cpyimagingmspec/badge/?version=latest)](http://cpyimagingmspec.readthedocs.org/en/latest/?badge=latest)

Scoring imaging mass spectrometry images for multiple isotopes.

## Installation

Binary builds are provided for convenience, use 
- `easy_install cpyImagingMSpec` on Linux
- `pip install cpyImagingMSpec` on OS X.

If it didn't work for you or you have security concerns, here's how to install the package from source:
- Install `cmake` and a recent version of `g++`, preferably 5.3
  - OS X: `brew install gcc5`
  - Ubuntu: install `gcc-5` package from `ubuntu-toolchain-r` PPA
- Run `./make_osx_wheel.sh` or `./make_linux_egg.sh` and install whatever has been created in the `dist/` directory using `pip`

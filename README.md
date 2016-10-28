# cpyImagingMSpec [![Documentation Status](https://readthedocs.org/projects/cpyimagingmspec/badge/?version=latest)](http://cpyimagingmspec.readthedocs.org/en/latest/?badge=latest)

Scoring imaging mass spectrometry images for multiple isotopes.

## Installation

Binary builds are provided for convenience, use `pip install cpyImagingMSpec`.
(You might have to run `pip install --upgrade pip` first, its version should be at least `8.1.1`.)

If it didn't work for you or you have security concerns, here's how to install the package from source:
- Install `cmake` and a recent version of `g++`, preferably 5.3
  - make sure submodules are loaded ``` git submodule update --init ```
  - OS X: 
    - `brew install gcc cmake`
    - Run `./make_osx_wheel.sh`
  - Ubuntu: 
    - install dependancies
        - `gcc-5` package from `ubuntu-toolchain-r` PPA
    
        ``` 
        sudo add-apt-repository ppa:ubuntu-toolchain-r/test
        sudo apt-get update
        sudo apt-get install gcc-5 g++-5
        ```
        - docker
        ```
        apt-get install docker.io
        ```
    - Do compile
    ```
    sudo bash wheel_builders/make_linux_wheel.sh ims-cpp ims_cffi
    ``` 
  - Install whatever has been created in the `dist/` directory using `pip`

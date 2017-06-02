from setuptools import setup, find_packages
from shutil import copyfile
import os
import glob

# before building the wheel, appropriate wheel_builders script must be run

VERSION = "0.2.4"

rtd = os.environ.get('READTHEDOCS', None) == 'True'

extra_files = {
    os.path.join('ims-cpp', 'cffi', 'ims.h'):
    os.path.join('cpyImagingMSpec', 'ims.h')
}

if not rtd:
    shared_lib_filename = glob.glob("ims-cpp/build/libims_cffi*")[0]
    extra_files.update({
        shared_lib_filename:
        os.path.join('cpyImagingMSpec', os.path.basename(shared_lib_filename))
    })
    package_data = {'cpyImagingMSpec': [shared_lib_filename, 'ims.h']}
else:
    package_data = {}

for src, dst in extra_files.items():
    copyfile(src, dst)

setup(
    name='cpyImagingMSpec',
    version=VERSION,
    author='Artem Tarasov',
    author_email='artem.tarasov@embl.de',
    url='https://github.com/alexandrovteam/cpyImagingMSpec',
    license='Apache 2.0',
    description='utils for processing imaging mass spectrometry data',
    packages=find_packages(where='.'),
    package_data=package_data,
    setup_requires=['wheel>=0.27.0'],
    install_requires=[] if rtd else ['cffi>=1.7', 'numpy>=1.10', 'pandas>=0.18'],

    ext_modules=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ]
)

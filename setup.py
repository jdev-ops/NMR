from setuptools import setup, find_packages
import unittest

from torch.utils.cpp_extension import BuildExtension, CUDAExtension

CUDA_FLAGS = []
INSTALL_REQUIREMENTS = []

def test_all():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

ext_modules=[]

setup(
    description='PyTorch implementation of "A 3D mesh renderer for neural networks"',
    author='Nikolaos Kolotouros',
    author_email='nkolot@seas.upenn.edu',
    license='MIT License',
    version='1.1.3',
    name='neural_renderer_pytorch',
    test_suite='setup.test_all',
    packages=['neural_renderer', 'neural_renderer.cuda'],
    install_requires=INSTALL_REQUIREMENTS,
    ext_modules=ext_modules,
    cmdclass = {'build_ext': BuildExtension}
)

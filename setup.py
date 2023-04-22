from distutils.core import setup

import numpy

required = [
    "sympy",
    "pandas",
    "click",
    "tqdm",
]

setup(name='scibench',
      version='1.0',
      setup_requires=["numpy", "Cython"],
      include_dirs=[numpy.get_include()],
      install_requires=required,
      )

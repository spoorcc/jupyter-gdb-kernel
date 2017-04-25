from setuptools import setup

setup(name='jupyter_c_kernel',
      version='0.0.1',
      description='GDB kernel for Jupyter',
      author='Ben Spoor',
      author_email='gdb-kernel@spoor.cc',
      url='https://github.com/spoorcc/jupyter-gdb-kernel/',
      download_url='https://github.com/spoorcc/jupyter-gdb-kernel/tarball/0.0.1',
      packages=['jupyter_gdb_kernel'],
      keywords=['jupyter', 'kernel', 'gdb'],
      install_requires=['jupyter'],
      )

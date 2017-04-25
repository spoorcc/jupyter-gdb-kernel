# GDB kernel for Jupyter Notebooks

This kernel can be used to show GDB commands in Jupyter Notebooks

## Installation

Make sure gdb version 7+ is installed on notebook server location

```shell
python3 -m venv venv
pip install -e .
jupyter-kernelspec install spec/kernel.json
```

## Usage

```shell
gcc test/dummy.c -g -o dummy
jupyter notebook --port=8080 --ip=0.0.0.0 --no-browser
gdbserver 0.0.0.0:1234 dummy
```

## Development

TODO

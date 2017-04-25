from ipykernel.kernelapp import IPKernelApp
from .kernel import GDBKernel
IPKernelApp.launch_instance(kernel_class=GDBKernel)

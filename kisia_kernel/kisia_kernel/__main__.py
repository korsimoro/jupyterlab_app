from ipykernel.kernelapp import IPKernelApp
from .kernel import KisiaKernel
IPKernelApp.launch_instance(kernel_class=KisiaKernel)

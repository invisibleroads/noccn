import os
import sys


def add_path():
    sys.path.append(os.getenv(
        'CUDA_CONVNET', os.path.expandvars('$VIRTUAL_ENV/opt/cuda-convnet')))

add_path()


import convnet
import data
import gpumodel
import options
import shownet

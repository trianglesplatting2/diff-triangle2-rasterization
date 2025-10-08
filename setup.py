#
# The original code is under the following copyright:
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE_GS.md file.
#
# For inquiries contact george.drettakis@inria.fr
#
# The modifications of the code are under the following copyright:
# Copyright (C) 2025, University of Liege
# TELIM research group, http://www.telecom.ulg.ac.be/
# All rights reserved.
# The modifications are under the LICENSE.md file.
#
# For inquiries contact jan.held@uliege.be
#

from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import os
os.path.dirname(os.path.abspath(__file__))

setup(
    name="diff_triangle_rasterization",
    packages=['diff_triangle_rasterization'],
    ext_modules=[
        CUDAExtension(
            name="diff_triangle_rasterization._C",
            sources=[
            "cuda_rasterizer/rasterizer_impl.cu",
            "cuda_rasterizer/forward.cu",
            "cuda_rasterizer/backward.cu",
            "cuda_rasterizer/utils.cu",
            "rasterize_points.cu",
            "ext.cpp"],
            extra_compile_args={"nvcc": [
                "-I" + os.path.join(os.path.dirname(os.path.abspath(__file__)), "third_party/glm/"),
                "--use_fast_math",
            ]})
        ],
    cmdclass={
        'build_ext': BuildExtension
    }
)

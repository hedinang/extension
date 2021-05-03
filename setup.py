from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# setup(
#     name='upfirdn2d_op',
#     ext_modules=[
#         CUDAExtension('lltm_cuda', [
#             '/home/dung/Project/Python/test/upfirdn2d.cpp',
#             '/home/dung/Project/Python/test/upfirdn2d_kernel.cu',
#         ]),
#     ],
#     cmdclass={
#         'build_ext': BuildExtension
#     })

setup(
    name='fused',
    ext_modules=[
        CUDAExtension('fused', [
            '/home/dung/Project/Python/test/fused_bias_act.cpp',
            '/home/dung/Project/Python/test/fused_bias_act_kernel.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

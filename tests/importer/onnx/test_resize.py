# Copyright 2019-2021 Canaan Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# pylint: disable=invalid-name, unused-argument, import-outside-toplevel
import pytest
import os
import torch
import numpy as np
import sys
import test_util
import torchvision.transforms.functional as F

def _make_module(size, mode):

    class ResizeModule(torch.nn.Module):
        def __init__(self):
            super(ResizeModule, self).__init__()

        def forward(self, x):
            # x = torch.nn.functional.interpolate(x, size=size, scale_factor=scale_factor, mode=mode, align_corners=None, recompute_scale_factor=None)
            x = F.resize(x, size = size, interpolation = mode)
            return x

    return ResizeModule()

in_shapes = [
    [1, 3, 224, 224]
]

sizes = [
    (112, 112),
    (448, 448)
]

modes = [
    0, # PIL.Image.NEAREST
    # 2,   # PIL.Image.BILINEAR
]

@pytest.mark.parametrize('in_shape', in_shapes)
@pytest.mark.parametrize('size', sizes)
@pytest.mark.parametrize('mode', modes)
def test_concat(in_shape, size, mode, request):
    module = _make_module(size, mode)

    # test_util.test_onnx_module(request.node.name, module, in_shape, ['cpu', 'k210', 'k510'])
    test_util.test_onnx_module(request.node.name, module, in_shape, ['k510'])

if __name__ == "__main__":
    pytest.main(['-vv', 'test_reisze.py'])
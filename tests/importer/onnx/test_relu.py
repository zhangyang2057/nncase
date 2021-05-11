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

def _make_module():

    class ReluModule(torch.nn.Module):
        def __init__(self):
            super(ReluModule, self).__init__()
            self.relu = torch.nn.ReLU()

        def forward(self, x):
            x = self.relu(x)
            return x

    return ReluModule()

in_shapes = [
    [1],
    [8, 8],
    [1, 4, 16],
    [1, 3, 224, 224]
]

@pytest.mark.parametrize('in_shape', in_shapes)
def test_relu(in_shape, request):
    module = _make_module()

    # test_util.test_onnx_module(request.node.name, module, in_shape, ['cpu', 'k210', 'k510'])
    test_util.test_onnx_module(request.node.name, module, in_shape, ['k510'])

if __name__ == "__main__":
    pytest.main(['-vv', 'test_relu.py'])
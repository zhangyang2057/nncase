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

def _make_module(in_shape, padding, value):

    class PadModule(torch.nn.Module):
        def __init__(self):
            super(PadModule, self).__init__()
            self.pad = torch.nn.ConstantPad2d(padding, value)
            self.conv2d = torch.nn.Conv2d(in_shape[1], 3, 3)

        def forward(self, x):
            x = self.pad(x)
            x = self.conv2d(x)

            return x

    return PadModule()

in_shapes = [
    [1, 3, 60, 72],
    [1, 3, 224, 224]
]

paddings = [
    1,
    (1, 1, 1, 1),
    (0, 0, 0, 0),
    (3, 0, 2, 1)
]

values = [
    0
]

@pytest.mark.parametrize('in_shape', in_shapes)
@pytest.mark.parametrize('padding', paddings)
@pytest.mark.parametrize('value', values)
def test_pad(in_shape, padding, value, request):
    module = _make_module(in_shape, padding, value)

    # test_util.test_onnx_module(request.node.name, module, in_shape, ['cpu', 'k210', 'k510'])
    test_util.test_onnx_module(request.node.name, module, in_shape, ['k510'])

if __name__ == "__main__":
    pytest.main(['-vv', 'test_pad.py'])
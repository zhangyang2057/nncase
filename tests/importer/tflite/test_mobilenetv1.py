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
"""System test: test mobilenetv1"""
# pylint: disable=invalid-name, unused-argument, import-outside-toplevel
import pytest
import os
import tensorflow as tf
import numpy as np
import sys
import test_util


def _make_module(in_shape, alpha):
    return tf.keras.applications.MobileNet(in_shape, alpha, include_top=True)

in_shapes = [
    (224, 224, 3)
]

alphas = [
    1.0
]

@pytest.mark.parametrize('in_shape', in_shapes)
@pytest.mark.parametrize('alpha', alphas)
def test_mobilenetv1(in_shape, alpha, request):
    module = _make_module(in_shape, alpha)
    test_util.test_tf_module(request.node.name, module, ['cpu', 'k210', 'k510'])


if __name__ == "__main__":
    pytest.main(['-vv', 'test_mobilenetv1.py'])

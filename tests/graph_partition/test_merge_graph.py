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
import tensorflow as tf
import numpy as np
from tflite_test_runner import TfliteTestRunner


def _make_module():
    class Module(tf.Module):
        def __init__(self):
            super(Module).__init__()
            self.w1 = tf.constant(np.random.rand(
                1, 1, 6, 3).astype(np.float32) - 0.5)
            self.w2 = tf.constant(np.random.rand(
                1, 1, 6, 3).astype(np.float32) - 0.5)

        @tf.function(input_signature=[tf.TensorSpec([1, 4, 8, 3], tf.float32)])
        def __call__(self, x):
            out = tf.reshape(x, [1, 4, 4, 6])
            out1 = tf.nn.conv2d(out, self.w1, [1, 1], 'SAME')
            out2 = tf.nn.conv2d(out, self.w2, [1, 1], 'SAME')
            c1 = tf.concat([out1, out2], axis=3)
            return c1
    return Module()


def test_merge_graph(request):
    module = _make_module()

    runner = TfliteTestRunner(request.node.name)
    model_file = runner.from_tensorflow(module)
    runner.run(model_file)


if __name__ == "__main__":
    pytest.main(['-vv', 'test_merge_graph.py'])

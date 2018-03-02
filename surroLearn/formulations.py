#!/usr/bin/env python
# encoding: utf-8

import tensorflow as tf

from .utils import tensor_linear_interval_range
from .ops import L2


def linear_regularizer(lr1, lr2, steps):
    def reg(w, *_):
        lt = tensor_linear_interval_range(lr1, lr2, steps)
        loss = L2(w, lt)
        loss = tf.identity(loss, name="lambda_scale")
        return loss
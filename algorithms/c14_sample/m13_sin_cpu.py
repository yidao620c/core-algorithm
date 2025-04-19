#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# CPU正弦曲线
"""
    Topic: sample
    Desc : CPU正弦曲线
"""
import itertools
import math
import sys
import time

__author__ = 'Xiong Neng'

time_period = float(sys.argv[1]) if len(sys.argv) > 1 else 60  # seconds
time_slice = float(sys.argv[2]) if len(sys.argv) > 2 else 0.04  # seconds

N = int(time_period / time_slice)
for i in itertools.cycle(range(N)):
    busy_time = time_slice / 2 * (math.sin(2 * math.pi * i / N) + 1)
    t = time.clock() + busy_time
    while t > time.clock():
        pass
    time.sleep(time_slice - busy_time)

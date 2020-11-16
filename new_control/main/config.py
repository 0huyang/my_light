# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 10:49
# @Author  : Jaywatson
# @File    : config.py.py
# @Soft    : new_control
from __future__ import print_function
from __future__ import division
import os
from util.loadConf import config

con = config()
N_PIXELS = int(con.getOption('system', 'N_PIXELS'))
FPS = int(con.getOption('system', 'FPS'))
MIC_RATE = int(con.getOption('system', 'MIC_RATE'))
SOFTWARE_GAMMA_CORRECTION = False
GAMMA_TABLE_PATH = os.path.join(os.path.dirname(__file__), 'config/gamma_table.npy')

_max_led_FPS = int(((N_PIXELS * 30e-6) + 50e-6)**-1.0)
assert FPS <= _max_led_FPS, 'FPS must be <= {}'.format(_max_led_FPS)

MIN_FREQUENCY = 880
"""Frequencies below this value will be removed during audio processing"""

MAX_FREQUENCY = 1512
"""Frequencies above this value will be removed during audio processing"""

N_FFT_BINS = 24
"""Number of frequency bins to use when transforming audio to frequency domain

Fast Fourier transforms are used to transform time-domain audio data to the
frequency domain. The frequencies present in the audio signal are assigned
to their respective frequency bins. This value indicates the number of
frequency bins to use.

A small number of bins reduces the frequency resolution of the visualization
but improves amplitude resolution. The opposite is true when using a large
number of bins. More bins is not always better!

There is no point using more bins than there are pixels on the LED strip.
"""

N_ROLLING_HISTORY = 2
"""Number of past audio frames to include in the rolling window"""

MIN_VOLUME_THRESHOLD = 1e-3
"""No music visualization displayed if recorded audio volume below threshold"""
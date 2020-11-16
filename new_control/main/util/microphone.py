# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 22:42
# @Author  : Jaywatson
# @File    : microphone.py
# @Soft    : new_control
import time
import pyaudio
import numpy as np
from util.loadConf import config

p=pyaudio.PyAudio()

con = config()
MIC_RATE = int(con.getOption('system', 'MIC_RATE'))
FPS = int(con.getOption('system', 'FPS'))

#选择输入设备
def input_device():
    deviceList = {}
    for i in range(p.get_device_count()):
        if p.get_device_info_by_index(i)["maxInputChannels"] > 0 and p.get_device_info_by_index(i)["maxOutputChannels"] == 0:
            deviceList[p.get_device_info_by_index(i)["index"]] = p.get_device_info_by_index(i)["name"].encode('latin-1').decode('GBK')
    return deviceList

#启动录音串流
def start_stream(callback,index):
    # p = pyaudio.PyAudio()
    frames_per_buffer = int(MIC_RATE / FPS)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=MIC_RATE,
                    input_device_index=index,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    overflows = 0
    prev_ovf_time = time.time()
    while True:
        try:
            y = np.fromstring(stream.read(frames_per_buffer), dtype=np.int16)
            y = y.astype(np.float32)
            callback(y)
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    stream.stop_stream()
    stream.close()
    p.terminate()



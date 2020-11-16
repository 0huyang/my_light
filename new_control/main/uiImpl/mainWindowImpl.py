# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 21:21
# @Author  : Jaywatson
# @File    : mainWindowImpl.py
# @Soft    : new_control
from PyQt5.QtCore import pyqtSignal

from util import microphone, led, dsp
import config
import numpy as np
from ui.mainwindow import Ui_MainWindow
from uiImpl.noBorderImpl import noBorderImpl
from uiImpl.tipImpl import tipImpl
from PyQt5.QtWidgets import QMainWindow
import pyqtgraph as pg
import util.visualization as vs

class mainWindow(QMainWindow, Ui_MainWindow, noBorderImpl, tipImpl):
    index = pyqtSignal()

    # 初始化
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        #初始化
        self.deviceIndex = -1
        self.lightIP = ""
        self.lightPort = 0
        self.loadDevice()
        self.drawGraph()

        #按键关联
        self.sure_button.clicked.connect(self.startThread)
        self.stop_button.clicked.connect(self.stopThread)

    def loadDevice(self):
        deviceList = microphone.input_device()
        self.device_list.clear()
        self.device_list.addItem('请选择')
        for k, v in deviceList.items():
            self.device_list.addItem(v, k)  # 键、值反转

    def startThread(self):
        self.deviceIndex = self.device_list.itemData(self.device_list.currentIndex())
        if self.deviceIndex == None:
            self.deviceIndex = -1
            self.Tips("请选择设备")
            return
        self.lightIP = self.ip_edit.text()
        self.lightPort = self.port_edit.value()
        if self.lightIP != "..." or self.lightIP != "000.000.000.000":
            # if led.test_ip(self.lightIP,self.lightPort):
            #     from util.micThread import micSend
            #     self.micThread = micSend()
            #     self.index.connect(lambda: self.micThread.setIndex(self.deviceIndex))  # 通过信号槽设置时间
            #     self.index.emit()
            #     self.micThread.getCallbackSignal.connect(self.updateGraph)
            #     self.micThread.start()
            # else:
            #     self.Tips("请确认IP和端口是否正确")
            #     return
            from util.micThread import micSend
            self.micThread = micSend()
            self.index.connect(lambda: self.micThread.setIndex(self.deviceIndex))  # 通过信号槽设置时间
            self.index.emit()
            self.micThread.getCallbackSignal.connect(self.updateGraph)
            self.micThread.start()

    def stopThread(self):
        if self.micThread != None:
            self.micThread.terminate()
            del self.micThread

    def drawGraph(self):
        self.graphView = pg.GraphicsView(self.wave_widget)
        self.graphLayout = pg.GraphicsLayout(border=(100, 100, 100))
        self.graphView.setCentralItem(self.graphLayout)
        self.graphView.show()
        self.graphView.setWindowTitle('Visualization')
        self.graphView.resize(764, 528)
        # Mel filterbank plot
        fft_plot = self.graphLayout.addPlot(title='Filterbank Output', colspan=3)
        fft_plot.setRange(yRange=[-0.1, 1.2])
        fft_plot.disableAutoRange(axis=pg.ViewBox.YAxis)
        x_data = np.array(range(1, config.N_FFT_BINS + 1))
        self.mel_curve = pg.PlotCurveItem()
        self.mel_curve.setData(x=x_data, y=x_data * 0)
        fft_plot.addItem(self.mel_curve)
        # Visualization plot
        self.graphLayout.nextRow()
        led_plot = self.graphLayout.addPlot(title='Visualization Output', colspan=3)
        led_plot.setRange(yRange=[-5, 260])
        led_plot.disableAutoRange(axis=pg.ViewBox.YAxis)
        # Pen for each of the color channel curves
        r_pen = pg.mkPen((255, 30, 30, 200), width=4)
        g_pen = pg.mkPen((30, 255, 30, 200), width=4)
        b_pen = pg.mkPen((30, 30, 255, 200), width=4)
        # Color channel curves
        self.r_curve = pg.PlotCurveItem(pen=r_pen)
        self.g_curve = pg.PlotCurveItem(pen=g_pen)
        self.b_curve = pg.PlotCurveItem(pen=b_pen)
        # Define x data
        x_data = np.array(range(1, config.N_PIXELS + 1))
        self.r_curve.setData(x=x_data, y=x_data * 0)
        self.g_curve.setData(x=x_data, y=x_data * 0)
        self.b_curve.setData(x=x_data, y=x_data * 0)
        # Add curves to plot
        led_plot.addItem(self.r_curve)
        led_plot.addItem(self.g_curve)
        led_plot.addItem(self.b_curve)
        # Frequency range label
        self.freq_label = pg.LabelItem('')

        self.freq_slider = pg.TickSliderItem(orientation='bottom', allowAdd=False)
        self.freq_slider.addTick((config.MIN_FREQUENCY / (config.MIC_RATE / 2.0)) ** 0.5)
        self.freq_slider.addTick((config.MAX_FREQUENCY / (config.MIC_RATE / 2.0)) ** 0.5)
        self.freq_slider.tickMoveFinished = self.freq_slider_change
        self.freq_label.setText('Frequency range: {} - {} Hz'.format(
            config.MIN_FREQUENCY,
            config.MAX_FREQUENCY))


        #Create effect "buttons" (labels with click event)
        self.energy_label = pg.LabelItem('Energy')
        self.scroll_label = pg.LabelItem('Scroll')
        self.spectrum_label = pg.LabelItem('Spectrum')
        self.energy_label.mousePressEvent = self.energy_click
        self.scroll_label.mousePressEvent = self.scroll_click
        self.spectrum_label.mousePressEvent = self.spectrum_click
        self.energy_click(0)
        # Layout
        self.graphLayout.nextRow()
        self.graphLayout.addItem(self.freq_label, colspan=3)
        self.graphLayout.nextRow()
        self.graphLayout.addItem(self.freq_slider, colspan=3)
        self.graphLayout.nextRow()
        self.graphLayout.addItem(self.energy_label)
        self.graphLayout.addItem(self.scroll_label)
        self.graphLayout.addItem(self.spectrum_label)
        self.verticalLayout_5.addWidget(self.graphView)

    def updateGraph(self,y):
        mel = vs.microphone_update(y,self.lightIP,self.lightPort)
        if not mel is None:
            x = np.linspace(config.MIN_FREQUENCY, config.MAX_FREQUENCY, len(mel))
            self.mel_curve.setData(x=x, y=vs.fft_plot_filter.update(mel))
            # Plot the color channels
            self.r_curve.setData(y=led.pixels[0])
            self.g_curve.setData(y=led.pixels[1])
            self.b_curve.setData(y=led.pixels[2])

    def freq_slider_change(self,tick):
        minf = self.freq_slider.tickValue(0) ** 2.0 * (config.MIC_RATE / 2.0)
        maxf = self.freq_slider.tickValue(1) ** 2.0 * (config.MIC_RATE / 2.0)
        t = 'Frequency range: {:.0f} - {:.0f} Hz'.format(minf, maxf)
        self.freq_label.setText(t)
        config.MIN_FREQUENCY = minf
        config.MAX_FREQUENCY = maxf
        dsp.create_mel_bank()

    def energy_click(self,x):
        # Effect selection
        active_color = '#16dbeb'
        inactive_color = '#FFFFFF'
        vs.visualization_effect = vs.visualize_energy
        self.energy_label.setText('Energy', color=active_color)
        self.scroll_label.setText('Scroll', color=inactive_color)
        self.spectrum_label.setText('Spectrum', color=inactive_color)

    def scroll_click(self,x):
        # Effect selection
        active_color = '#16dbeb'
        inactive_color = '#FFFFFF'
        vs.visualization_effect = vs.visualize_scroll
        self.energy_label.setText('Energy', color=inactive_color)
        self.scroll_label.setText('Scroll', color=active_color)
        self.spectrum_label.setText('Spectrum', color=inactive_color)

    def spectrum_click(self,x):
        # Effect selection
        active_color = '#16dbeb'
        inactive_color = '#FFFFFF'
        vs.visualization_effect = vs.visualize_spectrum
        self.energy_label.setText('Energy', color=inactive_color)
        self.scroll_label.setText('Scroll', color=inactive_color)
        self.spectrum_label.setText('Spectrum', color=active_color)

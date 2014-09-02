# -*- coding: iso-8859-15 -*-
'''
Created on 05.03.2014

@author: Mussmann
'''

from psychopy import monitors, core, visual, event
#from pyTobiiCalibShapes import Cross, Disc, Quad
import pyTobii
import time

mon = monitors.Monitor('myMonitor')
window = visual.Window(size=mon.getSizePix(), color=(1,1,1), colorSpace='rgb', fullscr=True, monitor=mon, units='cm')

pyTobii.init(window, './', 'test')
pyTobii.calibrate(perfect=True)
pyTobii.showCalibrationResultPoints()

event.waitKeys()

pyTobii.showCalibrationResultNet()

event.waitKeys()

window.close()
core.quit()
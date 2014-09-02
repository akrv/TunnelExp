'''
Created on 26.02.2014

@author: Mussmann
'''

#import comtypes.client
#import win32com.client
#import pythoncom

import time
import pyTetClient
#import tobiiConfiguration

#tc = win32com.client.Dispatch("TobiiStudio.TetClient.2")

#===============================================================================
# pythoncom.CoInitialize()
# print "Creating object..."
# tc = comtypes.client.CreateObject("TobiiStudio.TetClient.2")
# pythoncom.CoUninitialize()
# 
# print "Connecting..."
# tc.Connect("localhost", 4455 , 3)
# 
# print "Connected: "+str(tc.IsConnected)
# 
# print "Start tracking..."
# tc.StartTracking()
# print "Tracking: "+str(tc.IsTracking)
# 
# print tc.GetNumPendingPostGazeData()
# print tc.GetTimeStamp()
# 
# tc.Disconnect()
# 
# print "Connected: "+str(tc.IsConnected)
#===============================================================================

eventSink = pyTetClient.TetClientEventSink()
tc = pyTetClient.pyTetClient(eventSink)

print "Connect..." 
tc.Connect("localhost", 4455, 3)
time.sleep(2)

print "Start tracking..."
tc.StartTracking()
time.sleep(2)

print "Stop tracking"
tc.StopTracking()
time.sleep(2)

print "Stop process"
tc.stopEventProcessing()
time.sleep(2)

print "Disconnect..."
tc.Disconnect()

print "finished"
# update GUI label from another thread
# http://stackoverflow.com/questions/10574821/dynamically-updating-tkinter-window-based-on-serial-data

from time import sleep
import threading
from Tkinter import *
import serial

class SensorThread(threading.Thread):
    def run(self):
        global serialdata
        while not terminate:
            if ser.inWaiting():
                serialdata = ser.readline()
                #print serialdata,' '
            sleep(0.1)
#--------------------------------------------------------------------
class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.lbl = Label(self.root, text=9999, font=("Arial", 72))
        self.root.minsize(width=320, height=140)
        self.root.maxsize(width=320, height=140)        
        self.lbl.pack()
        self.root.pack_propagate(0)        
        
    def  start(self):
        self.readSensor()
        self.root.mainloop()

    def readSensor(self):
        self.lbl["text"] = serialdata.strip()
        self.root.update()
        self.root.after(500, self.readSensor)

#--------------------------------------------------------------------
serialdata = "0000"
ser = serial.Serial('COM4', 9600, timeout=0)

terminate = False
SensorThread().start()
Gui().start()
terminate = True  
 
print 'Bye !' 
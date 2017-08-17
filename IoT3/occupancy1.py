# update GUI bulb from serial port; log it in a CSV file with time stamp.
# use it with 

from time import sleep
import threading
from PyQt4 import QtCore 
from Tkinter import *
from PIL import ImageTk, Image
import serial

class SensorThread(threading.Thread):
    def run(self):
        global serialdata
        try:
            while not terminate:
                    if ser.inWaiting():
                        serialdata = ser.readline()
                        print serialdata,' '
        except Exception as e:
            print(e)
#--------------------------------------------------------------------
class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.onlogo = ImageTk.PhotoImage(Image.open("lamp-on.jpg"))
        self.offlogo = ImageTk.PhotoImage(Image.open("lamp-off.jpg"))
        #self.lbl = Label(self.root, text=" 0 ", font=("Arial", 180))
        self.lbl = Label(self.root, image=self.offlogo)
        self.root.minsize(width=460, height=740)
        self.status = -2
        self.prevstatus = -2
        self.lbl.pack()
        self.root.pack_propagate(0)
        
    def go(self):
        self.readSensor()
        self.root.mainloop()

    def writeTS(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        f.write (text +',')
        
    def readSensor(self):
        try:
            dat = serialdata.strip()
            if (dat[0] == 'R'):
                self.status = -1
            else:
                if (dat >= '0' and dat <= '9'):
                    self.status = int(dat)
            if (self.status != self.prevstatus): 
                 self.prevstatus = self.status
                 if (self.status==1):
                    self.lbl['image'] = self.onlogo
                 else:
                    self.lbl['image'] = self.offlogo
                 self.root.update()
                 self.writeTS()
                 f.write (str(self.status) +'\n')
            self.root.after(30, self.readSensor)
        except Exception as e:
            print(e)
            self.root.after(30, self.readSensor)

#--------------------------------------------------------------------
serialdata = "0"
data = True
terminate = False
f = open("log1.csv", "w")

ser = serial.Serial('COM5', 9600, timeout=0)
SensorThread().start()
Gui().go()
 
terminate = True   
f.close()
print 'Bye !' 
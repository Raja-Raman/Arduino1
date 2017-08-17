# # update GUI bulb from serial port-from another thread
# http://stackoverflow.com/questions/10574821/dynamically-updating-tkinter-window-based-on-serial-data

from time import sleep
import threading
from Tkinter import *
from PIL import ImageTk, Image
import serial

class SensorThread(threading.Thread):
    def run(self):
        global serialdata
        while not terminate:
            if ser.inWaiting():
                serialdata = ser.readline()
                #print serialdata,' '
            #sleep(0.2)
#--------------------------------------------------------------------
class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.onlogo = ImageTk.PhotoImage(Image.open("lamp-on.jpg"))
        self.offlogo = ImageTk.PhotoImage(Image.open("lamp-off.jpg"))
        #self.lbl = Label(self.root, text=" 0 ", font=("Arial", 180))
        self.lbl = Label(self.root, image=self.offlogo)
        self.root.minsize(width=460, height=740)
        self.status = 0
        self.lbl.pack()
        self.root.pack_propagate(0)
        
    def go(self):
        self.readSensor()
        self.root.mainloop()

    def readSensor(self):
        try:
            self.status = int(serialdata.strip()) // TODO: this continuously updates th GUI;save previous status instead
            if (self.status==0):
                self.lbl['image'] = self.offlogo
            else:
                self.lbl['image'] = self.onlogo
            self.root.update()
            self.root.after(30, self.readSensor)
        except Exception as e:
            print(e)

#--------------------------------------------------------------------
serialdata = "0"
data = True
terminate = False

ser = serial.Serial('COM5', 9600, timeout=0)
SensorThread().start()
Gui().go()
 
terminate = True   
print 'Bye !' 
# GUI clock in PyTK  
# http://stackoverflow.com/questions/10574821/dynamically-updating-tkinter-window-based-on-serial-data

from time import sleep
import threading
from PyQt4 import QtCore, QtGui
from Tkinter import *
import serial


class SensorThread(threading.Thread):
    def run(self):
        global serialdata
        while not terminate:
            if ser.inWaiting():
                serialdata = ser.readline()
                #print serialdata,' '
            sleep(0.2)
#--------------------------------------------------------------------
class Gui(object):
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(True)
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        print 'w=', w, ', h=', h
        self.root.geometry("{0}x{1}+0+0".format(w, h))       
        self.lbl = Label(self.root, text=9999, font=("Arial", 360), bg="black", fg="yellow")
        self.lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.root.configure(bg='black')
        self.root.bind("<Escape>", lambda e: e.widget.quit())
        self.readSensor()

    def go(self):
        #self.lbl.pack()
        self.root.pack_propagate(0)
        #self.root.minsize(width=1200, height=700)
        self.root.mainloop()

    def readSensor(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + '.' + text[3:]    
        self.lbl["text"] = text
        self.root.update()
        self.root.after(980, self.readSensor)

#--------------------------------------------------------------------
serialdata = "0000"
data = True
terminate = False

#ser = serial.Serial('COM3', 9600, timeout=0)
#SensorThread().start()
Gui().go()
 
terminate = True
sleep(0.2)
print 'Bye !' 
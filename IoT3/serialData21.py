# receive serial data (use with repeaterX.ino)
 

import serial

port = 'COM5'  # 'COM7'
    
logger = open ('serial_data1.txt','wt')
ser = serial.Serial(port, 9600, timeout=0) 
           
print 'Press ^C to exit...\n'
try:
    while True:
        if ser.inWaiting():
            c = ser.read()      
            print c, ord(c)
except KeyboardInterrupt:
    pass
    
print 'Bye !' 

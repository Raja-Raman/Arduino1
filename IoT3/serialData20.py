# receive serial ultrasonic ranger data and display on the console (use with ultra6.ino)
 

import serial

port = 'COM6'  # 'COM7'
    
sound_log = open ('sound_data.txt','wt')
ser = serial.Serial(port, 9600, timeout=0) 
           
print 'Press ^C to exit...\n'
try:
    while True:
        if ser.inWaiting():
            c = ser.read() 
            #print c.encode('hex') 
            #print ord(c)       
            n = ord(c)
            if (n>100): n=100
            for i in range(n):
                print '=',
            #print ' ',
            print n
except KeyboardInterrupt:
    pass
    
print 'Bye !' 

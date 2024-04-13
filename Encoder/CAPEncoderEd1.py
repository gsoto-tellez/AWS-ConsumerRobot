from time import sleep
from as5600 import *

i2c = I2C(0,scl=Pin(22),sda=Pin(21),freq=400000)        

  
z = AS5600(i2c,AS5600_id)
z.scan()
whatever = 89
while True:
    print ('ZANGLE',z.RAWANGLE)
    print ('ANGLE', z.ANGLE)
    print ('Magnet detected',z.MD)
    sleep(1)

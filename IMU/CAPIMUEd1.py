from machine import Pin, SoftI2C
from math import sqrt, atan2, pi, copysign, sin, cos
from mpu9250 import MPU9250
from time import sleep

#adresses
MPU = 0x68
sda = Pin(21)
scl = Pin(22)

# creating the I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

# scanning the bus
print(i2c.scan())
m = MPU9250(i2c)

while True:
    print("x", m.acceleration[0], "y", m.acceleration[1], "z", m.acceleration[2])
    print("Gyroscope X, Y, Z (deg/s):", m.gyro[0], m.gyro[1], m.gyro[2])
    sleep(1)

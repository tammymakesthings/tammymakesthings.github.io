import time

import adafruit_icm20x
import board

i2c = board.I2C()  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20649(i2c)

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    print("")
    time.sleep(0.5)

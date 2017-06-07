# import sensor from library
# code from: github.com/adafruit/adafruit_python_tcs34725/blob/master/examples/simpletest.py
import time
import smbus

bus = smbus.SMBus(1)

# Adafruit TCS34725 is on I2C address 0x29
# Register 0x12 has device version.
# Register addresses must be Or'ed with 0x80
bus.write_byte(0x29, 0x80|0x12)
ver = bus.read_byte(0x29)
# Our version number is not the same as the version number described in the blogpost
# The solution is to first print the ver to make sure you have the correct version number
# So our ver is 68 instead of 44

# We can read the colorsensor data if the version number is 68
if ver == 68:
		print("Device found\n")
		bus.write_byte(0x29, 0x80|0x00)         # 0x00 = the ENABLE register
		bus.write_byte(0x29, 0x01|0x02)         # 0x01 = power on, 0x02 RGB sensor enable
		bus.write_byte(0x29, 0x80|0x14)         # Reading results start at 0x14
		while True:
				data = bus.read_i2c_block_data(0x29, 0)
				red = data[3] << 8 | data[2]
				green = data[5] << 8 | data[4]
				blue = data[7] << 8 | data[6]
				red = red / 256         # Devide the data by 256 to make it a 
				green = green / 256     # 8-bit value. This makes the look up
				blue = blue / 256       # easier.
				print('R: {0}   G: {1}    B: {2}'.format(red, green, blue))
				time.sleep(1)
# If the device version is not 68...
else:
		print("Device not found")

#import sensor from library
#code from: github.com/adafruit/adafruit_python_tcs34725/blob/master/examples/simpletest.py
import time
import smbus

bus = smbus.SMBus(1)

bus.write_byte(0x29, 0x80|0x12)
ver = bus.read_byte(0x29)

if ver == 68:
		print("Device found\n")
		bus.write_byte(0x29, 0x80|0x00)
		bus.write_byte(0x29, 0x01|0x02)
		bus.write_byte(0x29, 0x80|0x14)
		while True:
				data = bus.read_i2c_block_data(0x29, 0)
				red = data[3] << 8 | data[2]
				green = data[5] << 8 | data[4]
				blue = data[7] << 8 | data[6]
				red = red / 256
				green = green / 256
				blue = blue / 256
				print('R: {0}   G: {1}    B: {2}'.format(red, green, blue))
				time.sleep(1)
else:
		print("Device not found")

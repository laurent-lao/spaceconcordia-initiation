# Author: Laurent Lao
# Read voltage from serial (Arduino), convert it into temperature
# and print it

import serial

def convert_into_temperature(sensor, sensor_const):

	# 0-1023 into 0.0-5.0 voltage value
	voltage = sensor * (0.004882812)

	# debug
	print(" Voltage: " + str(voltage))

	# voltage into celcius
	celcius = (voltage - sensor_const) * 100.0

	return celcius

# Accessing Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Ensuring it worked
print(ser.name)

# Looping reading
while True:
	readval = float(ser.readline())
	print("Sensor value: " + str(readval) + " Celcius: " + str(convert_into_temperature(readval, 0.25)))
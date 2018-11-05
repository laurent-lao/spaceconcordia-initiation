import serial

# Testing reading sensor values from Arduino

# Accessing Arduino
ser = serial.Serial('/dev/ttyUSB0')

# Ensuring it worked
print(ser.name)

# Looping reading
while True:
	readval = ser.readline()
	print("Sensor value: " + readval)


import serial
from flask import *
import time

# Create a Flask object
app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def whatever():
		




if __name__ == '__main__':
	# laucnh webpage
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	app.run()

/********
 * Author: Laurent Lao
 * With help from SparkFun Inventor's Kit:
 * Allows for temperature sensor to be read from pyserial
 * Sensor sends voltage data from 0 to 1026
 */

// Intiatizing analog input 0 to measure sensor signal pin

const int temperaturePin = A0;

void setup() {
  
  // Start port and set baud to 9600
  Serial.begin(9600);
  
}

void loop() {

  //Data obtained is between 0 and 1023
  float reading;
  reading = analogRead(temperaturePin)

  //Output data
  Serial.print(reading);

  //Repeat once per second
  delay(1000);
}

/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* Crated by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/

// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 13;

// defines variables
long duration;
int distance;
int threshold = 100;  // in Cm

void setup() {
	pinMode(ledPin , OUTPUT); // Sets the led Pin as an Output
	pinMode(trigPin, OUTPUT); // Sets the trigger Pin as an Output
	pinMode(echoPin, INPUT);  // Sets the echo Pin as an Input
	Serial.begin(9600);       // Starts the serial communication
}

void loop() {

	// prepare the trigPin
	digitalWrite(trigPin, LOW);
	delayMicroseconds(2);
	// Sets the trigPin on HIGH state for 10 micro seconds
	digitalWrite(trigPin, HIGH);
	delayMicroseconds(10);
	digitalWrite(trigPin, LOW); 

	// Reads the echoPin, returns the sound wave travel time in microseconds
	duration = pulseIn(echoPin, HIGH);

	// Calculating the distance
	distance= duration*0.034/2;

	// Prints the distance on the Serial Monitor
	Serial.print("Distance: ");
	Serial.println(distance);

	// indicate proximity
	if (distance < threshold)
		digitalWrite(ledPin, HIGH);
	else
		digitalWrite(ledPin, LOW);
}


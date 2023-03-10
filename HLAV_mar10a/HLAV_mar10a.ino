/*
-----------------------------
HLAV Version 1.0
Programer: Nikola Ciric 
-----------------------------
*/


//Ultrasonic sensor pin definitions

#define FRONT_TRIG_1 23
#define FRONT_ECHO_1 22

#define FRONT_TRIG_2 25
#define FRONT_ECHO_2 24

#define RIGHT_TRIG_1 27
#define RIGHT_ECHO_1 26

#define RIGHT_TRIG_2 29
#define RIGHT_ECHO_2 28


#define LEFT_TRIG_1 35
#define LEFT_ECHO_1 34

#define LEFT_TRIG_2 37
#define LEFT_ECHO_2 36

#define BACK_TRIG_1 33
#define BACK_ECHO_1 32

#define BACK_TRIG_2 31
#define BACK_ECHO_2 30

//Declare variables
long duration, distance, FrontSensor1,FrontSensor2,RightSensor1, RightSensor2, LeftSensor1, LeftSensor2, BackSensor1, BackSensor2;

void setup()
{
Serial.begin (9600);

//set pin modes

pinMode(FRONT_TRIG_1, OUTPUT);
pinMode(FRONT_ECHO_1, INPUT);

pinMode(FRONT_TRIG_2, OUTPUT);
pinMode(FRONT_ECHO_2, INPUT);

pinMode(RIGHT_TRIG_1, OUTPUT);
pinMode(RIGHT_ECHO_1, INPUT);

pinMode(RIGHT_TRIG_2, OUTPUT);
pinMode(RIGHT_ECHO_2, INPUT);


pinMode(LEFT_TRIG_1, OUTPUT);
pinMode(LEFT_ECHO_1, INPUT);

pinMode(LEFT_TRIG_2, OUTPUT);
pinMode(LEFT_ECHO_2, INPUT);

pinMode(BACK_TRIG_1, OUTPUT);
pinMode(BACK_ECHO_1, INPUT);

pinMode(BACK_TRIG_2, OUTPUT);
pinMode(BACK_ECHO_2, INPUT);
}

void loop() {

FrontSensor1 = CalculateDistance(FRONT_TRIG_1, FRONT_ECHO_1 );
FrontSensor2 = CalculateDistance(FRONT_TRIG_2, FRONT_ECHO_2);
RightSensor1 = CalculateDistance(RIGHT_TRIG_1,RIGHT_ECHO_1 );
RightSensor2 = CalculateDistance(RIGHT_TRIG_2,RIGHT_ECHO_2 );
LeftSensor1 = CalculateDistance(LEFT_TRIG_1,LEFT_ECHO_1 );
LeftSensor2 = CalculateDistance(LEFT_TRIG_2,LEFT_ECHO_2 );
BackSensor1 = CalculateDistance(BACK_TRIG_1,BACK_ECHO_1 );
BackSensor2 = CalculateDistance(BACK_TRIG_2,BACK_ECHO_2 );

Serial.print(FrontSensor1);
Serial.print(" - ");
Serial.print(FrontSensor2);
Serial.print(" - ");
Serial.print(RightSensor1);
Serial.print(" - ");
Serial.print(RightSensor2);
Serial.print(" - ");
Serial.print(LeftSensor1);
Serial.print(" - ");
Serial.print(LeftSensor2);
Serial.print(" - ");
Serial.print(BackSensor1);
Serial.print(" - ");
Serial.println(BackSensor2);
}

long CalculateDistance(int trigPin,int echoPin) // Function to calculate distance 
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;
return distance;
}


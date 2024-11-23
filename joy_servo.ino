#include <Servo.h>

int but = 2;
int butdurum;
Servo motor;
Servo motor1;

int degery;
int derecey;
int degerx;
int derecex;

#define led 8

void setup() {
  motor.attach(3);
  Serial.begin(9600);
  motor1.attach(6);
  pinMode(but, INPUT_PULLUP);
  pinMode(led , OUTPUT);
}

void loop() {
  butdurum = digitalRead(but);
  if
  (digitalRead(2) == 0){
  degery = analogRead(A0);
  derecey = map(degery , 0 , 1023 , 0 ,1023);
  motor.write(degery);
  Serial.print("y == ");
  Serial.println(derecey);


  degerx = analogRead(A1);
  derecex = map(degerx , 0 , 1023 , 0 ,1023);
  motor1.write(degerx);
   Serial.print("x == ");
   Serial.println(derecex);
  
  Serial.print(digitalRead(butdurum));
  }


  if 
      (analogRead(A0) < 520){
      digitalWrite(led,1);
  }

  if 
    (digitalRead(2) == 0){
      digitalWrite(led ,1);
    }
   else

     digitalWrite(led,0);
    
}

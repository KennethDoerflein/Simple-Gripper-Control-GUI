// Python with arduino Servo control 
#include <Servo.h>

String value;
const char delim = ';';
char buffer[4];
int bufferIndex;

Servo servo;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1); 
  servo.attach (9);
  bufferIndex = 0;   
  servo.write(180);
  delay(500);
  servo.write(0);
  delay(500);
}

void readBuffer(){
  if (Serial.available()){
    char c = Serial.read();
    buffer[bufferIndex] = c;
    bufferIndex++;
  }
}

void parseBuffer(){
  if (buffer[bufferIndex-1] == ';'){
    buffer[bufferIndex-1] = '\0';
    int newData = atoi(buffer);
    if (newData != 0 && newData != 180){
      int currentAngle = servo.read();
      int newAngle = currentAngle + newData;
      servo.write(newAngle);
    } else {
      servo.write(newData);
    }
    flushBuffer();
  }
}

void flushBuffer(){
  Serial.flush();
  bufferIndex = 0;
  for (int i = 0; i < sizeof(buffer); i++) {
    buffer[i] = -1;
  }
}

void loop() {
  readBuffer();
  parseBuffer(); 
}
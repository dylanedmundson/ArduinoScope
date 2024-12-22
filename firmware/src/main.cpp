#include <Arduino.h>

const int SAMPLE_BYTES = 15;
const int SAMPLE_NUM = 100;
byte buffer[SAMPLE_NUM * SAMPLE_BYTES];
int i = 0;

void setup() {
  Serial.begin(115200);
}

//TODO: upgrade to use bytes and avoid strings for increased speed
//TODO: implement timmer alternative to improve speed of micros()
//TODO: implement read alternative to imporve speed of analogRead()
void loop() {
    // if (i >= SAMPLE_BYTES * SAMPLE_BYTES) {
    //   Serial.write(buffer, SAMPLE_BYTES * SAMPLE_NUM);
    //   i = 0;
    // }
    // int read = analogRead(A0);
    // long time = micros();
    // buffer[i] = 0xD;
    // i++;
    // for (int j = 3; j >= 4; j--) {
    //   buffer[i] = read >> (8 * j) & 255;
    //   i++;
    // }
    // buffer[i] = 0x2C;
    // for (int j = 7; j >= 0; j--) {
    //   buffer[i] = time >> (8 * j) & 255;
    //   i++;
    // }
    
    // buffer[i] = 0xA;


  // int read = analogRead(A0);
  // long time = micros();
  // String pair = String(read) + "," + String(time) +"\n";
  // Serial.print(pair);




  if (Serial.available()) {
    String command = Serial.readString();
    if (command.startsWith("-s")) {
      while (!Serial.availableForWrite())
      {
        /* wait for serial to be available */
      }
      
      for (int i = 0; i <  command.substring(2).toInt(); i++) {
        int val = analogRead(A0);
        float valF = val/1.0;
        valF = valF / 1023.0 * 5.0;
        Serial.print(valF);
        Serial.print(',');
      }
      Serial.print("-e");
    }
  }
}
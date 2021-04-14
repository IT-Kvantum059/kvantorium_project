#include <Servo.h>

#define INIT 0
#define IDLE 1
#define EXEC 2
#define INIT_POS 0

#ifndef SERVO_1_PIN
#define SERVO_1_PIN 5
#endif

#ifndef SERVO_2_PIN
#define SERVO_2_PIN 6
#endif

Servo myservo1; // назначаем вывод 1 сервы
Servo myservo2; // назначаем вывод 2 сервы


char incomingByte = 0;
int pos = 0;
char comand[3];
char *p;

int state = INIT;
void setup()
{

  // устанавливаем пин как вывод управления сервой

  //инициализация последовательного порта:
  Serial.begin(9600);
}

void loop() {
  switch (state) {
    case INIT:
      myservo1.attach(SERVO_1_PIN);
      myservo2.attach(SERVO_2_PIN);
      myservo1.write(INIT_POS);
      myservo2.write(INIT_POS);
      state = IDLE;
      break;
    case IDLE:
      if (Serial.available() > 0) { //если есть доступные данные - считываем байт
        comand[0] = Serial.read();
        comand[1] = Serial.read();
        state = EXEC;
        *p = comand;
      }
      break;
    case EXEC:
      Serial.println(p);
      break;
    default:
      break;
  }

}

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


char *p;
int newpos = 0;
int servonumber = 0;

int state = INIT;
void setup()
  {
      Serial.begin(9600); //инициализация последовательного порта
  }

void loop() {
  switch (state) {
     case INIT:
        myservo1.attach(SERVO_1_PIN);
        myservo2.attach(SERVO_2_PIN);
        myservo1.write(INIT_POS);
        myservo2.write(INIT_POS);
        Serial.println("Enter rotation angle");
        state = IDLE;
        break;
     case IDLE:
        if (Serial.available() > 0) { //если есть доступные данные - считываем байт
            newpos = Serial.parseInt();
            state = EXEC;
         }
        break;
     case EXEC:
        if (newpos < 2000) {
             myservo1.write(newpos - 1000); //поворот первой сервы на заданный угол
             state = IDLE;
        }
        else {
             myservo2.write(newpos - 2000); //поворот второй сервы на заданный угол
             state = IDLE;
        }
        break;
        default:
         break;
}

}

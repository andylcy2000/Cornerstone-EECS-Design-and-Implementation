/***************************************************************************/
// File       [final_project.ino]
// Author     [Erik Kuo]
// Synopsis   [Code for managing main process]
// Functions  [setup, loop, Search_Mode, Hault_Mode, SetState]
// Modify     [2020/03/27 Erik Kuo]
/***************************************************************************/

#define DEBUG // debug flag

// for RFID
#include <SPI.h>
#include <MFRC522.h>
#include <string.h>
#include <SoftwareSerial.h>
/*===========================define pin & create module object================================*/
// BlueTooth
// BT connect to BT (Hardware Serial)
// Mega               HC05
// Pin  (Function)    Pin
// 18    TX       ->  RX
// 19    RX       <-  TX
// TB6612, 請按照自己車上的接線寫入腳位(左右不一定要跟註解寫的一樣)
#define AIN1      2 //定義 A1 接腳（右）
#define AIN2      3 //定義 A2 接腳（右）
#define PWMA    11//定義 ENA (PWM調速) 接腳
#define BIN1      5 //定義 B1 接腳（左）
#define BIN2      6 //定義 B2 接腳（左）
#define PWMB    12//定義 ENB (PWM調速) 接腳
SoftwareSerial BT (10, 11);
// 循線模組, 請按照自己車上的接線寫入腳位
int IRpin_LL = 32;
int IRpin_L  = 34;
int IRpin_M  = 36;
int IRpin_R  = 38;
int IRpin_RR = 40;
// RFID, 請按照自己車上的接線寫入腳位
#define RST_PIN      9        // 讀卡機的重置腳位
#define SS_PIN       53       // 晶片選擇腳位
MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件
/*===========================define pin & create module object===========================*/

/*============setup============*/
void setup()
{
   //bluetooth initialization
   BT.begin(9600);
   //Serial window
   Serial.begin(9600);
   //RFID initial
   SPI.begin();
   mfrc522.PCD_Init();
   //TB6612 pin
   pinMode(AIN1,   OUTPUT);
   pinMode(AIN2,   OUTPUT);
   pinMode(BIN1,   OUTPUT);
   pinMode(BIN2,   OUTPUT);
   pinMode(PWMA, OUTPUT);
   pinMode(PWMB, OUTPUT);
   //tracking pin
   pinMode(IRpin_LL, INPUT); 
   pinMode(IRpin_L, INPUT);
   pinMode(IRpin_M, INPUT);
   pinMode(IRpin_R, INPUT);
   pinMode(IRpin_RR, INPUT);
#ifdef DEBUG
  Serial.println("Start!");
#endif
}
/*============setup============*/

/*=====Import header files=====*/
#include "RFID.h"
#include "track.h"
#include "bluetooth.h"
#include "node.h"
/*=====Import header files=====*/

/*===========================initialize variables===========================*/
int l2=0,l1=0,m0=0,r1=0,r2=0; //紅外線模組的讀值(0->white,1->black)
int _Tp=90; //set your own value for motor power
bool state=false; //set state to false to halt the car, set state to true to activate the car
BT_CMD _cmd = NOTHING; //enum for bluetooth message, reference in bluetooth.h line 2
byte idSize = 0;
int s[1000];
int count = 0;
int j = 0;
int l_speed = 220;//205
int r_speed = 220;//220
int apple = 0;
/*===========================initialize variables===========================*/

/*===========================declare function prototypes===========================*/
void Search();// search graph
void SetState(int l2,int l1,int m0,int r1,int r2);// switch the state
/*===========================declare function prototypes===========================*/

/*===========================define function===========================*/
void loop()
{
  send_byte(rfid(idSize), idSize);
  if (BT.available()) {
    int tmp = BT.read();
    if (tmp == 's') {
      state = true;
    } else if (tmp == 'e') {
      state = false;
      stop();
    } else {
      s[j] = tmp;
      j++;
    }
  }  
  if (state) {
    l2 = digitalRead(IRpin_LL);
    l1 = digitalRead(IRpin_L);
    m0 = digitalRead(IRpin_M);
    r1 = digitalRead(IRpin_R);
    r2 = digitalRead(IRpin_RR);
    if (l2 && l1 && m0 && r1 && r2) {      
      switch(s[count]){
        case 'f':
          forward(0);
          delay(650);
          break;
        case 'l':
          turn_left();
          break;
        case 'r':
          turn_right();
          break;
        case 'b':
          u_turn_right();
          break;
      }
      sendString();
      count++;
    } else {
      // if (l2 && l1) forward(-2);
      // else if (l2) forward(-3);
      // else if (l1) forward(-1);
      // else if (r2 && r1) forward(2);
      // else if (r2) forward(3);
      // else if (r1) forward(1);
      // else forward(0);
      forward(-2 * l2 - 1 * l1 + r1 + 2 * r2);
    }
  } else {
    stop();
  }
  // if(!state) MotorWriting(0,0);
  // else Search();
  // SetState(l2,l1,m0,r1,r2);
}
void SetState(int l2,int l1,int m0,int r1,int r2)
{
  // TODO:
  // 1. Get command from bluetooth
   
  // 2. Change state if need
  
}

void Search()
{
  // TODO: let your car search graph(maze) according to bluetooth command from computer(python code)
}

void forward(double power) {
  // if (power == 2) power = 3;
  // // else if (power == 3) power = 2;
  // else if (power == -2) power = -3;
  // // else if (power == -3) power = -2;
  // if (power > 0) {
  //   analogWrite(PWMA, l_speed - (l_speed - 100 - apple) * (power / 3));
  //   analogWrite(PWMB, l_speed + (255 - l_speed) * (power / 3));
  // } else {
  //   analogWrite(PWMA, r_speed + (255 - r_speed) * (power / 3));
  //   analogWrite(PWMB, r_speed - (r_speed - 100 - apple) * (power / 3));    
  // }
  if (power > 0) {
    analogWrite(PWMA, l_speed - (l_speed - 0 - apple)/* * (power / 3)*/);
    analogWrite(PWMB, l_speed + (255 - l_speed)/* * (power / 3)*/);
  } else if (power < 0) {
    analogWrite(PWMA, r_speed + (255 - r_speed)/* * (power / 3)*/);
    analogWrite(PWMB, r_speed - (r_speed - 0 - apple)/* * (power / 3)*/);    
  } else {
    analogWrite(PWMA, r_speed);
    analogWrite(PWMB, l_speed);    
  }
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
}

void backward() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
}

void turn_left() {
  analogWrite(PWMA, 255);
  analogWrite(PWMB, 110);
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  delay(900);
  while (!(digitalRead(IRpin_M) || digitalRead(IRpin_R) || digitalRead(IRpin_RR))) {}
}

void turn_right() {
  analogWrite(PWMA, 110);
  analogWrite(PWMB, 255);
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  delay(900);
  while (!(digitalRead(IRpin_LL) || digitalRead(IRpin_L) || digitalRead(IRpin_M))) {}
}

void u_turn_right() {
  analogWrite(PWMA, 170);
  analogWrite(PWMB, 170);
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
  delay(300);
  while (!digitalRead(IRpin_M)) {}
}

void stop() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
}

/*===========================define function===========================*/

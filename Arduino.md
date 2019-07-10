<img src="https://latex.codecogs.com/svg.latex?y=x^2\hbox{when&space;$x>2$}" />

<img src="https://latex.codecogs.com/svg.latex?x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}"/>

- [Display](#Display)
  - [TFT 2.4" China](#tft-24-china--arduino-due)

# Display
## TFT 2.4" China & Arduino DUE
Dùng thư viện Adafruit_GFX và MCUFRIEND_kbv
Quan trọng: Trong Setup: `tft.begin(0x9341);` quên cái init tft này thì không chạy.

```cpp
#define LCD_CS A3 // Chip Select goes to Analog 3
#define LCD_CD A2 // Command/Data goes to Analog 2
#define LCD_WR A1 // LCD Write goes to Analog 1
#define LCD_RD A0 // LCD Read goes to Analog 0
#define LCD_RESET A4 // Can alternately just connect to Arduino's reset pin

#include "Adafruit_GFX.h"// Hardware-specific library
#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;

void setup(void) {
  tft.begin(0x9341);
  tft.setCursor(0, 10);
  tft.println(" GRG Subway In-Out System");
  ...
}
```

<details>
<summary>Full code, các thư viện download trên mạng mặc định là dc.</summary>
  
<p>

```cpp
#define LCD_CS A3 // Chip Select goes to Analog 3
#define LCD_CD A2 // Command/Data goes to Analog 2
#define LCD_WR A1 // LCD Write goes to Analog 1
#define LCD_RD A0 // LCD Read goes to Analog 0
#define LCD_RESET A4 // Can alternately just connect to Arduino's reset pin

#include <SPI.h>          // f.k. for Arduino-1.5.2
#include "Adafruit_GFX.h"// Hardware-specific library
#include <MCUFRIEND_kbv.h>
MCUFRIEND_kbv tft;
//#include <Adafruit_TFTLCD.h>
//Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);

// Assign human-readable names to some common 16-bit color values:
#define	BLACK   0x0000
#define	BLUE    0x001F
#define	RED     0xF800
#define	GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

#ifndef min
#define min(a, b) (((a) < (b)) ? (a) : (b))
#endif

void setup(void);
void loop(void);
unsigned long testFillScreen();
unsigned long testText();
unsigned long testLines(uint16_t color);
unsigned long testFastLines(uint16_t color1, uint16_t color2);
unsigned long testRects(uint16_t color);
unsigned long testFilledRects(uint16_t color1, uint16_t color2);
unsigned long testFilledCircles(uint8_t radius, uint16_t color);
unsigned long testCircles(uint8_t radius, uint16_t color);
unsigned long testTriangles();
unsigned long testFilledTriangles();
unsigned long testRoundRects();
unsigned long testFilledRoundRects();
void progmemPrint(const char *str);
void progmemPrintln(const char *str);

void runtests(void);

uint16_t g_identifier;

extern const uint8_t hanzi[];


//-------------------------------------------------------------
//-------------------------------------------------------------
String inputString = "";         // a String to hold incoming data
String inputString_old = "";
bool stringComplete = false;  // whether the string is complete
bool FirstTimeRun = true;
//-------------------------------------------------------------
//-------------------------------------------------------------
void init_screen() {
  tft.fillScreen(BLACK);
  tft.setTextColor(CYAN); tft.setTextSize(2);
  tft.setCursor(0, 10);
  tft.println(" GRG Subway In-Out System");
  tft.setCursor(92, 40);
  tft.println("Version 1.0");


  tft.setCursor(115, 60); tft.setTextSize(1);
  tft.println("Nguyen Tuan Anh");
  tft.setTextColor(YELLOW); tft.setTextSize(2);

}
#define btAuto 53
#define btMenu 51
#define btOnOF 49
void setup(void) {
  Serial.begin(57600);
  uint32_t when = millis();
  if (!Serial) delay(5000);           //allow some time for Leonardo
  //Serial.println("Serial took " + String((millis() - when)) + "ms to start");
  //    tft.reset();                 //hardware reset
  //uint16_t ID = tft.readID(); //
  //Serial.print("ID = 0x");
  //Serial.println(ID, HEX);
  //if (ID == 0xD3D3) ID = 0x9481; // write-only shield
  //    ID = 0x9329;                             // force ID
  Serial.println("GRG_subway_TFT24inch\n\r;");
  tft.begin(0x9341);
  pinMode(btAuto, INPUT_PULLUP);
  pinMode(btMenu, INPUT_PULLUP);
  pinMode(btOnOF, INPUT_PULLUP);

  tft.setRotation(1);
  init_screen();
  inputString.reserve(200);
}

//-------------------------------------------------------------
//-------------------------------------------------------------
//-------------------------------------------------------------
//-------------------------------------------------------------
int vAuto0 = HIGH;
int vMenu0 = HIGH;
int vOnOF0 = HIGH;
int waitsending = 0;
const int WSt = 1000;
void loop(void) {
  // Button:=======================================
  int vAuto = digitalRead(btAuto);
  int vMenu = digitalRead(btMenu);
  int vOnOF = digitalRead(btOnOF);

  if (waitsending > 0) {
    waitsending--;
  }
  if (waitsending == 0) {
    if ((vAuto0 == HIGH) && (vAuto == LOW)) {
      Serial.print("Start;"); waitsending = WSt;
    }
    if ((vMenu0 == HIGH) && (vMenu == LOW)) {
      Serial.print("Stop;"); waitsending = WSt;
    }
    if ((vOnOF0 == HIGH) && (vOnOF == LOW)) {
      init_screen();
    }    
  }
  vAuto0 = vAuto;
  vMenu0 = vMenu;
  vOnOF0 = vOnOF;
  // END Button:==================================

  if (stringComplete) {
#define TOP 100
    tft.setCursor(0, TOP);
    tft.setTextColor(BLACK);
    tft.println(inputString_old);

    tft.setCursor(0, TOP);
    tft.setTextColor(YELLOW);

    tft.println(inputString);
    inputString_old = inputString;
    inputString = "";
    stringComplete = false;
  }
}
//-------------------------------------------------------------
//-------------------------------------------------------------
//-------------------------------------------------------------
//-------------------------------------------------------------
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();

    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
    else {
      inputString += inChar;
      // add it to the inputString:
    }
  }
  if (FirstTimeRun) {
    //tft.fillScreen(BLACK);
    FirstTimeRun = false;
  }
}
```

</p>
</details>  




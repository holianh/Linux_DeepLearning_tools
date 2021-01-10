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


# Send/receive data to server HTTPS
## Wifiduino từ EPS8266:
Code này nạp vào arduino :
Key code, code tối thiểu để chạy được:
```c++
#define USING_AXTLS
#include <ESP8266WiFi.h>
#include <WiFiClientSecureAxTLS.h>
using namespace axTLS;
#ifndef STASSID
#define STASSID "Khong-Co-Mang"
#define STAPSK  "06122015"
#endif
const char* ssid     = STASSID;
const char* password = STAPSK;
const char* host = "aisolutions.vn"; // online
// Open host web, Lclick a lock on left of address>certificate>detail>Thumbprint
const char fingerprint[] = "58f32f2e18e23ed2fa6e04c7b287e9c41db638a5"; 
const int httpsPort = 443;
WiFiClientSecure client;
void setup() {
	Serial.begin(115200);
	WiFi.mode(WIFI_STA);
	WiFi.begin(ssid, password);
	while (WiFi.status() != WL_CONNECTED){delay(500);Serial.print(".");}
	Serial.println(WiFi.localIP());
	if (!client.connect(host, httpsPort)){Serial.println("connection failed");delay(5000);return;}
	if (client.verify(fingerprint, host)){Serial.println("certificate matches");} 
	else {Serial.println("certificate doesn't match");}

	String url = "/test/post-get.php?id=1&value=Mot";
	client.print(String("GET ") + url + " HTTP/1.1\r\n" +
	 "Host: " + host + "\r\n" +
	 "User-Agent: BuildFailureDetectorESP8266\r\n" +
	 "Connection: close\r\n\r\n");
	while (client.connected()) {String line = client.readStringUntil('\n'); if (line == "\r") {break;}}
	while(client.available()){
	  String line = client.readStringUntil('\n');
	  Serial.println(line);
	  if(line.substring(0,7) == "Success"){Serial.write("Thanh cong");}}
	client.stop();
}
void loop() {
}
```
<details>
    <summary>Full code Wifiduino </summary>
  
```c++
#define USING_AXTLS
#include <ESP8266WiFi.h>
// https://www.youtube.com/watch?v=QKVK9Z6BiEc&ab_channel=EngineeringOnline
// force use of AxTLS (BearSSL is now default)
#include <WiFiClientSecureAxTLS.h>
using namespace axTLS;

#ifndef STASSID
#define STASSID "Khong-Co-Mang"
#define STAPSK  "06122015"
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;

//const char* host = "192.168.1.13"; // my local host IPaddress running XAMPP web control
const char* host = "aisolutions.vn"; // online
// Open host web, Lclick a lock on left of address>certificate>detail>Thumbprint
const char fingerprint[] = "58f32f2e18e23ed2fa6e04c7b287e9c41db638a5"; 
const int httpsPort = 443;

WiFiClientSecure client;
static bool wait = false;
static int cnt= 0;
static int WFconnected= false;

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.print("connecting to ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  if (!client.connect(host, httpsPort)) {
    Serial.println("connection failed");
    delay(5000);
    return;
  }

  if (client.verify(fingerprint, host)) {
    Serial.println("certificate matches");
    WFconnected=true;
    } else {
      Serial.println("certificate doesn't match");
    }

    String url = "/test/post-get.php?id=1&value=Mot";
    Serial.print("requesting URL: ");
    Serial.println(url);

    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
     "Host: " + host + "\r\n" +
     "User-Agent: BuildFailureDetectorESP8266\r\n" +
     "Connection: close\r\n\r\n");

    Serial.println("request sent");
    while (client.connected()) {
      String line = client.readStringUntil('\n');
      if (line == "\r") {
        Serial.println("headers received");
        break;
      }
    }
    while(client.available()){
      String line = client.readStringUntil('\n');
      Serial.println(line);
      if(line.substring(0,7) == "Success")
      {
        Serial.write("Thanh cong");
      }
    }
    Serial.println("closing connection");
    client.stop();
  }

  void SendProcess(){
    if (!client.connect(host, httpsPort)) {
      Serial.println("connection failed");
      delay(5000);
      return;
    }

    if (client.verify(fingerprint, host)) {
      // Serial.println("certificate matches");
      WFconnected=true;
      } else {
        Serial.println("certificate doesn't match");
      }

      String url = "/test/post-get.php?id="+String(cnt)+"&value=Mot";
      Serial.print("requesting URL: ");
      Serial.println(url);
      cnt=(cnt+1)%4;
      client.print(String("GET ") + url + " HTTP/1.1\r\n" +
       "Host: " + host + "\r\n" +
       "User-Agent: BuildFailureDetectorESP8266\r\n" +
       "Connection: close\r\n\r\n");

      // Serial.println("request sent");
      while (client.connected()) {
        String line = client.readStringUntil('\n');
          // Serial.println("headers received===================");
          // Serial.print(line);
          // Serial.println("===================================");
          if (line == "\r") {
          break;
        }
      }
      while(client.available()){
        String line = client.readStringUntil('\n');
        Serial.println(line);
        if(line.substring(0,7) == "Success")
        {
          Serial.write("Thanh cong");
        }
      }
      // Serial.println("closing connection");
      client.stop();
    }
void loop() {
 SendProcess();
  if (wait) {
   delay(3000); // execute once every xxx, don't flood remote service
  }
  wait = true;
}

```
 

</details>


## Code PHP server:
Còn đây là code để up lên server:
<details>
  
<summary>Full code</summary>

```PHP
<?php 

// PHP code:
$IDs_Values = array(
  '0' => 'Khong',
  '1' => 'Mot',
  '2' => 'Hai',
  );
if (isset($_GET['id'])) {
    if (isset($_GET['value'])) {
          	$id=$_GET['id'];
          	$value=$_GET['value'];
          	if(array_key_exists($id, $IDs_Values)){
          		http_response_code(200);

          		echo 'Success: exist id='.$id.' in array()!<br/>';
	          	if (in_array ($value, $IDs_Values)){	              	
	              	echo 'exist value='.$value.' in that array<br/>';
	              	echo '<br/>Successful !!!';
	            }else{
	            	echo 'Success: value='.$value.' not exist in array';
	            }
          	}else{              
              	http_response_code(333);
              	echo "Failed: id not i data ...";
              	echo 'id='.$id.' value='.$value;
          	}   
          	die(0);       
    }
    http_response_code(333); // khác 200 là lỗi.
    echo "Failed:  Errors ...having id without value?";
    die(0);
}
// Cách dùng: http://localhost/test/post-get.php?id=1&value=Mot

?>
```

</p>

</details>
Đấy chỉ có vậy thôi!

# Send/receive data to server HTTP hoặc local file
## Wifiduino từ EPS8266:





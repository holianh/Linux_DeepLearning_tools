
# Send/receive data to server HTTPS
## Wifiduino từ EPS8266:
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
//
//void loop() {
//  static bool wait = false;
//
//  Serial.print("connecting to ");
//  Serial.print(host);
//  Serial.print(':');
//  Serial.println(port);
//
//  // Use WiFiClient class to create TCP connections
//  WiFiClient client;
//  if (!client.connect(host, port)) {
//    Serial.println("connection failed");
//    delay(5000);
//    return;
//  }
//
//  // This will send a string to the server
//  Serial.println("sending data to server");
//  String url = "/test/post-get.php?id=1&value=Mot";
//        Serial.print("Requesting URL: ");
//        Serial.println(url);
//        
//        // This will send the request to the server
//        client.print(String("GET ") + url + " HTTP/1.1\r\n" +
//                     "Host: " + host + "\r\n" + 
//                     "Connection: close\r\n\r\n");
//        unsigned long timeout = millis();
//        while (client.available() == 0) {
//          if (millis() - timeout > 5000) {
//            Serial.println(">>> Client Timeout !");
//            client.stop();
//            return;
//          }
//        }
//        
//        // Read all the lines of the reply from server and print them to Serial
//        while(client.available()){
//          String line = client.readStringUntil('\n');
//          Serial.println(line);
//          if(line.substring(0,7) == "Success")
//          {
//            Serial.write("Thanh cong");
//          }
//        }
//        Serial.println();
//        Serial.println("closing connection");
//        
//  client.stop();
//
//  if (wait) {
//    delay(30000); // execute once every 5 minutes, don't flood remote service
//  }
//  wait = true;
//}
```

## Code PHP server:

```PHP
<?php 

// PHP code:
$IDs_Values = array('0' => 'Khong',
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

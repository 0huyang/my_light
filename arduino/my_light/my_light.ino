/*************************************************************
  Support by guagua
  注意:带*的位置，必须修改为你自己的参数。
  资料来源于:https://www.makeuseof.com/tag/computer-lighting-nodemcu-wifi/
  blynk:https://www.blynk.cc
  arduino:https://www.arduino.cc/
  FastLED:http://fastled.io/
*************************************************************/

#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <Arduino.h>
#include <BlynkSimpleEsp8266.h>
#include <WebSocketsServer.h>
#include <Hash.h>
#include <WiFiUdp.h>
#include <NeoPixelBus.h>

//---FastLED 参数---
#define NUM_LEDS 120 //* LED灯数量，根据你的情况做修改。
#define LED_TYPE WS2812B //灯带型号，一般不需要改变
#define COLOR_ORDER GRB //颜色指令
#define BUFFER_LEN 1024
#define PRINT_FPS 1

//---RGB颜色值 (0-255) ---
int r = 255;
int g = 255;
int b = 255;
float led_bright = 1;

int websocket = 0;

//--主开关和彩虹模式变量
int masterSwitch = 0;
int mode = 1;

//NeoPixelBus settings
const uint8_t PixelPin = 3;  // make sure to set this to the correct pin, ignored for Esp8266(set to 3 by default for DMA)

// Wifi and socket settings
const char* ssid     = "first floor";
const char* password = "qwertyuiop";
unsigned int localPort = 7777;
char packetBuffer[BUFFER_LEN];

// LED strip
NeoPixelBus<NeoGrbFeature, Neo800KbpsMethod> ledstrip(NUM_LEDS, PixelPin);

WiFiUDP port1;

// Network information
// IP must match the IP in config.py
IPAddress ip(192, 168, 123, 123);
// Set gateway to your router's gateway
IPAddress gateway(192, 168, 123, 1);
IPAddress subnet(255, 255, 255, 0);

//---WIFI设置和BLYNK服务器和验证码---
char auth[] = "4c33413711b542d8a185a4bc5badb017";//* blynk验证码，在blynk APP中获取
char server[] = "106.14.220.77";  //BLYNK服务器地址，请勿修改，除非你有自己的BLYNK服务器
int port = 8080; //ESP8266连接BLYNK服务器端口，请勿修改

void setup() {

  // 开关保护延迟
  delay(2000);
  Serial.begin(115200);

  //---ESP8266 WIFI设置和Blynk验证码以及服务器地址 ---
  Blynk.begin(auth, ssid, password, server, port);

  WiFi.config(ip, gateway, subnet);
  WiFi.begin(ssid, password);
  Serial.println("");
  // Connect to wifi and print the IP address over serial
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  port1.begin(localPort);
  ledstrip.Begin();//Begin output
  ledstrip.Show();//Clear the strip for use

}
void(* resetFunc) (void) = 0;

BLYNK_CONNECTED() {
  Blynk.syncAll();
}

uint8_t N = 0;
#if PRINT_FPS
uint16_t fpsCounter = 0;
uint32_t secondTimer = 0;
#endif

void loop() {
  // Read data over socket
  int packetSize = port1.parsePacket();
  // If packets have been received, interpret the command
  websocket = 0;
  if (packetSize) {
    websocket = 1;
    int len = port1.read(packetBuffer, BUFFER_LEN);
    for (int i = 0; i < len; i += 4) {
      packetBuffer[len] = 0;
      N = packetBuffer[i];
      RgbColor pixel((uint8_t)packetBuffer[i + 1], (uint8_t)packetBuffer[i + 2], (uint8_t)packetBuffer[i + 3]);
      ledstrip.SetPixelColor(N, pixel);
    }
    ledstrip.Show();
#if PRINT_FPS
fpsCounter++;
Serial.print("/");//Monitors connection(shows jumps/jitters in packets)
#endif
}
if (websocket == 0) {
Blynk.run();
if (masterSwitch == 0) {
for (int i = 0; i < NUM_LEDS; i++) {
ledstrip.SetPixelColor(i, RgbColor((uint8_t)0, (uint8_t)0, (uint8_t)0));
}
ledstrip.Show();
}
if (mode == 1 && masterSwitch == 1) {
for (int i = 0; i < NUM_LEDS; i++) {
ledstrip.SetPixelColor(i, HslColor(183.0f, 0.0f, led_bright));
}
ledstrip.Show();
}

    if (mode == 2 && masterSwitch == 1) {
      for (int i = 0; i < NUM_LEDS ; i++) {
        RgbColor pixel((uint8_t)r, (uint8_t)g, (uint8_t)b);
        ledstrip.SetPixelColor(i, HslColor(pixel));
      }
      ledstrip.Show();
    }
    if (mode == 3 && masterSwitch == 1) {
      for (int y = 0; y < 360; y++) { //360 shades - NeoPixelBus uses float
        for (int x = 0; x <= NUM_LEDS; x++) { //NUM_LEDS
          ledstrip.SetPixelColor(x, HslColor(y / 360.0f, 0.8f, 0.25f));
        }
        ledstrip.Show();
      }
    }
  }
#if PRINT_FPS
if (millis() - secondTimer >= 1000U) {
secondTimer = millis();
Serial.printf("FPS: %d\n", fpsCounter);
fpsCounter = 0;
}
#endif
}

  //---主开关 Button---
  BLYNK_WRITE(V0) {
    masterSwitch = param.asInt();
  }

  //--- 红色 色值控制 Slider ---
  BLYNK_WRITE(V1) {
    r = param.asInt();
  }

  //--- 绿色 色值控制 Slider ---
  BLYNK_WRITE(V2) {
    g = param.asInt();
  }

  //--- 蓝色 色值控制 Slider ---
  BLYNK_WRITE(V3) {
    b = param.asInt();
  }

  //--- 彩虹/手动控制颜色 Button ---
  BLYNK_WRITE(V4) {
    mode = param.asInt();
  }

  //--- 亮度 Slider ---
  BLYNK_WRITE(V5) {
    led_bright = param.asFloat();
  }

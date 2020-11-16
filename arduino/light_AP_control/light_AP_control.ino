//--------库引用---------//
#include <EEPROM.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <FS.h>
#include <Arduino.h>
#include <SimpleTimer.h>
#include <BlynkSimpleEsp8266.h>
#include <Hash.h>
#include <WiFiUdp.h>
//#include <NeoPixelBus.h>
#include <NeoPixelBrightnessBus.h>


//--------变量定义---------//
SimpleTimer timer;//定时器
WiFiUDP port;
ESP8266WebServer server(80);

//---WIFI 参数---
int nNetwork = 0;
#define DEFAULT_STASSID ""
#define DEFAULT_STAPSW  ""
const char ssid[50] = "";
const char pwd[50] = "";
#define MAGIC_NUMBER 0xAA
//存储WiFi信息
struct config_type
{
  char stassid[50];
  char stapsw[50];
  uint8_t magic;
};
config_type config_wifi;

//是否执行联网后配置
bool Config = false;

//BLYNK服务器和验证码
bool Connected2Blynk = false;
char auth[] = "";//* blynk验证码，在blynk APP中获取
IPAddress blynk_server = IPAddress(0,0,0,0); //BLYNK服务器地址，请勿修改，除非你有自己的BLYNK服务器

//---LED 参数---
#define NUM_LEDS 60 //* LED灯数量，根据你的情况做修改。
//#define LED_TYPE WS2812B //灯带型号，一般不需要改变
//#define COLOR_ORDER GRB //颜色指令
#define BUFFER_LEN 1024
#define PRINT_FPS 1
int r = 255;
int g = 255;
int b = 255;

unsigned int musicPort = 7777;//音乐控制接口
char packetBuffer[BUFFER_LEN];
uint8_t N = 0;

//NeoPixelBus settings
const uint8_t PixelPin = 3;  // make sure to set this to the correct pin, ignored for Esp8266(set to 3 by default for DMA)

// LED strip
NeoPixelBrightnessBus<NeoGrbFeature, NeoEsp8266Dma800KbpsMethod> ledstrip(NUM_LEDS, PixelPin);

//---无线台灯 参数---
int masterSwitch = 0; //0为off,1为on
int lightMode = 1; //灯光模式
int ledBright = 50; //台灯亮度
float brightPer = 0.0; //亮度百分比

//--------函数定义---------//
// 设置内网
void ServerDef() {
  IPAddress softLocal(192, 168, 8, 1);
  IPAddress softGateway(192, 168, 8, 1);
  IPAddress softSubnet(255, 255, 255, 0);
  WiFi.softAPConfig(softLocal, softGateway, softSubnet);
  String apName(("ESP_" + (String)ESP.getChipId()));
  WiFi.softAP(apName.c_str());
  Serial.print("\nAP IP address: ");
  Serial.println(WiFi.softAPIP());
  Serial.print("softAPName: ");
  Serial.println(apName);

  server.on("/", handleMain);
  server.on("/wifi_ssid", handleWifiSsid);
  server.on("/wifi", handleSetWifi);
  server.on("/wifi_status", handleWifiStatus);
  server.onNotFound(handleNotFound);
  server.begin();
  nNetwork = WiFi.scanNetworks();
}

//首页
void handleMain() {
  Serial.print("handleMain");
  File file = SPIFFS.open("/index.html", "r");
  size_t sent = server.streamFile(file, "text/html");
  file.close();
  return;
}

//回填wifi ssid
void handleWifiSsid() {
  Serial.print("handleWifiSsid");
  String wifi_ssid = "";
  for (int i = 0; i < nNetwork; i++) {
    wifi_ssid += WiFi.SSID(i);
    if (i < nNetwork - 1) {
      wifi_ssid += ",";
    }
  }
  server.send(200, "text/plane", wifi_ssid);
}

//设置wifi
void handleSetWifi() {
  String wifi_ssid = server.arg(0);
  String wifi_pass = server.arg(1);
  wifi_ssid.toCharArray(config_wifi.stassid, 50);
  wifi_pass.toCharArray(config_wifi.stapsw, 50);
  if (!wifi_init()) {
    server.send(200, "text/plane", "fail");
  } else {
    server.send(200, "text/plane", "success");
  }
  saveConfig();
}

//网络状态
void handleWifiStatus() {
  String msg = "";
  IPAddress ip = WiFi.localIP();
  String temp = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
  if (WiFi.status() == WL_CONNECTED) {
    msg = WiFi.SSID() + "," + temp;
  } else {
    msg = "offline,";
  }
  server.send(200, "text/plane", msg);
}

//无对应请求
void handleNotFound() {
  String path = server.uri();
  Serial.print("load url:");
  Serial.println(path);
  String contentType = getContentType(path);

  if (SPIFFS.exists(path)) {
    File file = SPIFFS.open(path, "r");
    size_t sent = server.streamFile(file, contentType);
    file.close();
    return;
  } else {
    String message = "File Not Found\n\n";
    message += "URI: ";
    message += server.uri();
    message += "\nMethod: ";
    message += ( server.method() == HTTP_GET ) ? "GET" : "POST";
    message += "\nArguments: ";
    message += server.args();
    message += "\n";
    for ( uint8_t i = 0; i < server.args(); i++ ) {
      message += " " + server.argName ( i ) + ": " + server.arg ( i ) + "\n";
    }
    server.send ( 404, "text/plain", message );
  }
}

//判断请求类型
String getContentType(String filename) {
  if (server.hasArg("download")) return "application/octet-stream";
  else if (filename.endsWith(".htm")) return "text/html";
  else if (filename.endsWith(".html")) return "text/html";
  else if (filename.endsWith(".css")) return "text/css";
  else if (filename.endsWith(".js")) return "application/javascript";
  else if (filename.endsWith(".png")) return "image/png";
  else if (filename.endsWith(".gif")) return "image/gif";
  else if (filename.endsWith(".jpg")) return "image/jpeg";
  else if (filename.endsWith(".ico")) return "image/x-icon";
  else if (filename.endsWith(".xml")) return "text/xml";
  else if (filename.endsWith(".pdf")) return "application/x-pdf";
  else if (filename.endsWith(".zip")) return "application/x-zip";
  else if (filename.endsWith(".gz")) return "application/x-gzip";
  else return "text/plain";
}

//WIFI初始化
bool wifi_init() {
  Serial.print("\nConnected to ");
  Serial.println(config_wifi.stassid);
  WiFi.begin(config_wifi.stassid, config_wifi.stapsw);
  int t = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    t++;
    if (t > 20) {
      return false;
    }
  }
  Serial.print("\nIP address: ");
  Serial.println(WiFi.localIP());
  return true;
}

//存储wifi配置
void saveConfig()
{
  Serial.println("Save config!");
  Serial.print("stassid:");
  Serial.println(config_wifi.stassid);
  Serial.print("stapsw:");
  Serial.println(config_wifi.stapsw);
  EEPROM.begin(1024);
  uint8_t *p = (uint8_t*)(&config_wifi);
  for (int i = 0; i < sizeof(config_wifi); i++)
  {
    EEPROM.write(i, *(p + i));
  }
  EEPROM.commit();
}

//读取配置
void loadConfig()
{
  EEPROM.begin(1024);
  uint8_t *p = (uint8_t*)(&config_wifi);
  for (int i = 0; i < sizeof(config_wifi); i++)
  {
    *(p + i) = EEPROM.read(i);
  }
  EEPROM.commit();
  if (config_wifi.magic != MAGIC_NUMBER)
  {
    strcpy(config_wifi.stassid, DEFAULT_STASSID);
    strcpy(config_wifi.stapsw, DEFAULT_STAPSW);
    config_wifi.magic = MAGIC_NUMBER;
    saveConfig();
    Serial.println("Restore config!");
  }
  Serial.println(" ");
  Serial.println("-----Read config-----");
  Serial.print("stassid:");
  Serial.println(config_wifi.stassid);
  Serial.print("stapsw:");
  Serial.println(config_wifi.stapsw);
  Serial.println("-------------------");

  //  ssid=String(config.stassid);
  //  password=String(config.stapsw);
}

//检查Blynk是否在线
void CheckConnection() {
  Connected2Blynk = Blynk.connected();
  if (!Connected2Blynk) {
    //Serial.println("Not connected to Blynk server");
    Blynk.connect(3333);  // timeout set to 10 seconds and then continue without Blynk
  }
  else {
    //Serial.println("Connected to Blynk server");
  }
}

//台灯模式
void Lightfunc() {
  Blynk.virtualWrite(V1, 255);
  Blynk.virtualWrite(V2, 0);//台灯模式灯亮
  Serial.flush();
  if (masterSwitch == 1) {
    //Serial.println("-------on--------");
    switch (lightMode) {
      case 1:
        brightPer = 255 - ledBright;
        //Serial.println(brightPer);
        for (int i = 0; i < NUM_LEDS; i++) {
          RgbColor pixel((uint8_t)brightPer, (uint8_t)brightPer, (uint8_t)brightPer);
          ledstrip.SetPixelColor(i, HsbColor(pixel));
        }
        //ledstrip.SetBrightness(ledBright);
        ledstrip.Show();
        //Serial.println("-------台灯on--------");
        break;
      case 2:
        for (int i = 0; i < NUM_LEDS ; i++) {
          RgbColor pixel((uint8_t)r, (uint8_t)g, (uint8_t)b);
          ledstrip.SetPixelColor(i, HsbColor(pixel));
        }
        ledstrip.Show();
        break;
      case 3:
        for (int y = 0; y < 360; y++) { //360 shades - NeoPixelBus uses float
          for (int x = 0; x <= NUM_LEDS; x++) { //NUM_LEDS
            ledstrip.SetPixelColor(x, HslColor(y / 360.0f, 0.8f, 0.25f));
          }
          ledstrip.Show();
        }
        break;
      default: Serial.println("Mode ERR");
    }
  } else {
    for (int i = 0; i < NUM_LEDS; i++) {
      ledstrip.SetPixelColor(i, RgbColor((uint8_t)0, (uint8_t)0, (uint8_t)0));
    }
    ledstrip.Show();
    //Serial.println("-------off--------");
  }
}

void Musicfunc() {
  Blynk.virtualWrite(V2, 255);
  Blynk.virtualWrite(V1, 0);//音乐模式灯亮
  int len = port.read(packetBuffer, BUFFER_LEN);
  for (int i = 0; i < len; i += 4) {
     packetBuffer[len] = 0;
     N = packetBuffer[i];
     RgbColor pixel((uint8_t)packetBuffer[i + 1], (uint8_t)packetBuffer[i + 2], (uint8_t)packetBuffer[i + 3]);
     ledstrip.SetPixelColor(N, pixel);
  }
  ledstrip.Show();
}

//----Blynk 虚拟管脚定义----//
BLYNK_CONNECTED() {
  Blynk.syncAll();
}

//主开关 Button
BLYNK_WRITE(V0) {
  masterSwitch = param.asInt();
}

//模式选择 Button
BLYNK_WRITE(V4) {
  lightMode = param.asInt();
}

//亮度 Slider
BLYNK_WRITE(V5) {
  ledBright = param.asInt();
}

// rgb 调色 ---
BLYNK_WRITE(V6) {
  r = param[0].asInt();
  g = param[1].asInt();
  b = param[2].asInt();
}
//--------setup()---------//
void setup() {
  Serial.begin(115200);
  ledstrip.Begin();
  WiFi.mode(WIFI_AP_STA);
  WiFi.disconnect();
  SPIFFS.begin();
  loadConfig();// 读取信息 WIFI
  wifi_init();
  ServerDef();
}

//--------loop()---------//
void loop() {
  while (WiFi.status() == WL_CONNECTED) {
    if (!Config) {
      Serial.println("--- Online Config ---");
      port.begin(musicPort);
      Blynk.config(auth, blynk_server, 8080);
      Blynk.connect(3333);  //连接blynk服务器
      while (Blynk.connect() == false) {
        // Wait until connected
      }
      timer.setInterval(11000L, CheckConnection);
      Config = true;
    }
    Blynk.run();
    int packetSize = port.parsePacket();
    Serial.println(packetSize);
    if (packetSize) {
      Musicfunc();
    } else {
      Lightfunc();
    }
    timer.run();
    server.handleClient();
  }
//  server.handleClient();
}

#include<ESP8266WiFi.h>

String apiKey = "O74IMXCTQBZSJFYA";

const char *ssid = "corona";
const char *pass = "covid2019";
const char *server = "api.thingspeak.com";

WiFiClient client;
const int flamepin1 = 16;
const int flamepin2 = 5;
const int flamepin3 = 4;
const int flamepin4 = 0;
int danger;
int flame1;
int flame2;
int flame3;
int flame4;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
delay(10);

Serial.println("CONNECTING TO ");
Serial.println(ssid);

WiFi.begin(ssid, pass);

while (WiFi.status() != WL_CONNECTED)
{
  delay(500);
  Serial.print(".");
}
Serial.print("");
Serial.println("WiFi Connected");

pinMode(flamepin1, INPUT);
pinMode(flamepin2, INPUT);
pinMode(flamepin3, INPUT);
pinMode(flamepin4, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
flame1 = digitalRead(flamepin1);
flame2 = digitalRead(flamepin2);
flame3 = digitalRead(flamepin3);
flame4 = digitalRead(flamepin4);


if (client.connect(server,80))
{
  String postStr = apiKey;
  postStr += "&field1=";
  postStr += String(flame1);
  postStr += "&field2=";
  postStr += String(flame2);
  postStr += "&field3=";
  postStr += String(flame3);
  postStr += "&field4=";
  postStr += String(flame4);
  postStr += "\r\n\r\n";

  client.print("POST /update HTTP/1.1\n");
  client.print("Host: api.thingspeak.com\n");
  client.print("Connected: close\n");
  client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n");
  client.print("content-Type: application/x-www-form-urlencoded\n");
  client.print("content-Length: ");
  client.print(postStr.length());
  client.print("\n\n");
  client.print(postStr);


Serial.print("\n");
Serial.print("Sensor1 :");
Serial.print(flame1);
Serial.print(" Sensor2 :");
Serial.print(flame2);
Serial.print(" Sensor3 :");
Serial.print(flame3);
Serial.print(" Sensor4 :"); 
Serial.print(flame4);  
Serial.print("\n Sending value to Thingspeak.");
}
client.stop();

delay(1000);
}

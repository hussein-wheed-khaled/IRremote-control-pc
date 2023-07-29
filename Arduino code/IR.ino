#include <IRremote.h>
 
// Define sensor pin
const int RECV_PIN = 4;
 
// Define IR Receiver and Results Objects
IRrecv irrecv(RECV_PIN);
decode_results results;
unsigned long lastCode;

void setup(){
  // Serial Monitor @ 9600 baud
  Serial.begin(9600);
  // Enable the IR Receiver
  irrecv.enableIRIn();
}
 
void loop(){
 if(irrecv.decode(&results)) //this checks to see if a code has been received
{
 Serial.println(results.value, HEX);
    if(results.value == 0xFFFFFFFF)   
    {
       // If Repeat then use last code received
       results.value = lastCode;        
    }
 
    
      
    if(results.value == 0xFE9966 )     
    {
      
      Serial.println("up");
 
      
    }
 
   if(results.value == 0xFE39C6)     
    {
     Serial.println("left");   
    }

    
   if(results.value == 0xFE7986)     
    {
     Serial.println("right");   
    }

    
if(results.value == 0xFEB946 )     
    {
     Serial.println("down");   
    }

if(results.value == 0xFE59A6 )     
    {
     Serial.println("ok");   
    }
if (results.value==0xFE19E6){
  Serial.println("s-");
}
if (results.value==0xFED02F){
  Serial.println("s+");
}
 
   
    delay(30); 
   
    irrecv.resume(); 
}
    
}

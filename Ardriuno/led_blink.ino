#define led 13

void setup()
   {
   pinmode(led,OUTPUT);
   }
    
void loop()
   {
   digitalwrite(led,HIGH);
   delay(1000);
   digitalwrite(led,LOW);
   delay(1000);
   }
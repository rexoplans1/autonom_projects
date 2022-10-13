/*
 * Main içinde 2 task çalışacak. (cooperative multitasking)
1. task led on off yapacak. Örnek (300ms ON 700ms off) on off süreleri ayarlanabilir olacak. 
Nasıl ayarlanacağını aşağıdadır.    
2. task uart'tan gelen datayı aynı port üzerinden echo yapacak. Uart interrupt ile çalışacak ve ayarları değiştirilebilir olacak. default 115200 8N1
Uart'tan "stop" stringi gönderdiğimizde echo taskı sonlanacak ve led 1sn aralıklarla yanıp sönecek.
Uart'tan "start" stringi gönderdiğimizde echo taskı yeniden başlayacak ve led bir önceki ayarlarla çalışmaya devam edecek. 
Uart'tan "ledon=500" yazarsak led on süresi 500 ms olacak.
Uart'tan "ledoff=500" yazarsak led off süresi 500 ms olacak.
Bu 2 task birbirini bloke etmeyecek.
 * 
 */
 
/*
 * Variable Decleration
 */
String get_data;
unsigned long old_time=0;
unsigned long max_time=0,on_time=0,off_time=0; //max_tim=on_time+off_time
int echo_mode=0;
void setup() {
 
  /*
   * Init for led and Uart
   */
   pinMode(LED_BUILTIN,OUTPUT);
   Serial.begin(115200);
   //Start variable for led time   
   on_time=700;
   off_time=300;
   max_time=on_time+off_time;

}

void loop() {
  
  /*
   * Task-1 : Toggle Led
   */
    if(millis()-old_time>off_time)
  { 
    digitalWrite(LED_BUILTIN,1);
    if((millis()-old_time)>=max_time)
    {
      old_time=millis();
      digitalWrite(LED_BUILTIN,0);
    }
  }
  
   /*
    * Task-2 : Echo UART and Set Led ON/OFF Time
    */
    
  if(Serial.available()>0)
  {
    get_data=Serial.readString();
    //Serial.println(get_data);//For test 
    if(get_data=="start")
    {
      echo_mode=1;
    }
    else if(get_data=="stop")
    {
      echo_mode=0;
      unsigned long stop_off_time=1000;
      unsigned long stop_on_time=1000;
      max_time=stop_on_time+stop_off_time;
      Serial.println(max_time);
    }
    if(echo_mode==1)
    {
      Serial.println(get_data);
      max_time=on_time+off_time;
      int index_string=get_data.length();
      //Serial.println(index_string); //For Testing
      String check_on_string = get_data.substring(0,6); //"ledon="
      //Serial.println(check_on_string); //For Testing
      String check_off_string =get_data.substring(0,7); //"ledoff="
      //Serial.println(check_off_string); //For Testing
      if(check_on_string=="ledon=")
      {
        String timeon_value=get_data.substring(6,index_string);
        on_time=atol(timeon_value.c_str());
        //Serial.println(on_time);//For Testing
        max_time=on_time+off_time;
        //Serial.println(max_time);//For Testing
        
      }
      if(check_off_string=="ledoff=")
      {
        String timeoff_value=get_data.substring(7,index_string);
        off_time=atol(timeoff_value.c_str());
        //Serial.println(off_time);//For Testing
        max_time=on_time+off_time;
        //Serial.println(max_time);//For Testing
      }   
    }
  }

}

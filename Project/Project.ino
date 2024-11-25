int x;			//Variable to recieve data from Python
int Red_Pin= 11;	//RED LED
int Green_Pin = 9;	//GREEN LED
int Blue_Pin = 10;	//BLUE LED

void setup() 
{
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(Red_Pin, OUTPUT);
  pinMode(Green_Pin, OUTPUT);
  pinMode(Blue_Pin, OUTPUT);
}

void loop() 
{
  while (!Serial.available());
  x = Serial.readString().toInt();
//LED OFF if white
  if(x==0)
    setColor(0, 0, 0);
//RED
  else if(x==1)
    setColor(0,0,255);
//BLUE
  else if(x==2)
    setColor(255,0,0);
//GREEN
  else if(x==3)
    setColor(0,255,0);
//YELLOW
  else if(x==4)
    setColor(0,255,255);
//ORANGE
  else if(x==5)
    setColor(0,128,255);
//DEFAULT
  else
    setColor(0,0,0);
  Serial.print(x);
}

void setColor(int blueValue, int greenValue, int redValue)
{
  analogWrite(Red_Pin, redValue);
  analogWrite(Green_Pin, greenValue);
  analogWrite(Blue_Pin, blueValue);
}

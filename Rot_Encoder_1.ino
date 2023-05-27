// Adapted from https://projecthub.arduino.cc/raikanrule/encoder-volume-control-13b702
#define CLK 2 //values can be changed based on pin numbers
#define DT 3
#define SW 4

int counter = 0;
int currentStateCLK;
int lastStateCLK;
unsigned long lastButtonPress = 0;

void setup() {
  pinMode(CLK, INPUT);
  pinMode(DT, INPUT);
  pinMode(SW, INPUT_PULLUP);

  Serial.begin(9600);
  lastStateCLK = digitalRead(CLK);

}

void loop() {
  currentStateCLK = digitalRead(CLK);

  if (currentStateCLK != lastStateCLK && currentStateCLK == 1) {
    if (digitalRead(DT) != currentStateCLK) {
      counter++;

    }
    else {
      counter--;

    }

    Serial.println(counter);
  }

  lastStateCLK = currentStateCLK;

  delay(1);

}

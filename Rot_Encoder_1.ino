#define CLK 2
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
  Serial.println("This works");

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

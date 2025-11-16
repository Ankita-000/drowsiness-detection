/* alert_system.ino
   ESP32 firmware for 3-stage alert system
   Stage 1: LED
   Stage 2: LED + Buzzer
   Stage 3: LED + Buzzer + Vibration
*/

const int LED_PIN = 2;
const int BUZZER_PIN = 15;
const int VIBE_PIN = 13;

String inputString = "";

void setup() {
  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(VIBE_PIN, OUTPUT);

  digitalWrite(LED_PIN, LOW);
  digitalWrite(BUZZER_PIN, LOW);
  digitalWrite(VIBE_PIN, LOW);
}

void loop() {
  if (Serial.available()) {
    inputString = Serial.readStringUntil('\n');
    inputString.trim();

    if (inputString == "ALERT1") {
      stage1();
    } else if (inputString == "ALERT2") {
      stage2();
    } else if (inputString == "ALERT3") {
      stage3();
    }
  }
}

// ----------- STAGE 1 -------------
void stage1() {
  digitalWrite(LED_PIN, HIGH);
  delay(300);
  digitalWrite(LED_PIN, LOW);
}

// ----------- STAGE 2 -------------
void stage2() {
  stage1();
  digitalWrite(BUZZER_PIN, HIGH);
  delay(300);
  digitalWrite(BUZZER_PIN, LOW);
}

// ----------- STAGE 3 -------------
void stage3() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
    digitalWrite(VIBE_PIN, HIGH);
    delay(300);

    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(VIBE_PIN, LOW);
    delay(200);
  }
}

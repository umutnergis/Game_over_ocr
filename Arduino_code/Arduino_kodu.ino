int pin4 = 4;
int pin5 = 5;

void setup() {
  Serial.begin(9600);
  pinMode(pin4, OUTPUT);
  pinMode(pin5, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    
    char receivedChar = Serial.read();  // ASCII karakterini tamsayıya çevirir.
    Serial.println(receivedChar);
    if (receivedChar == 'A') {
      digitalWrite(pin4, HIGH);  // Pin 4'ü aktif hale getir
    } else if (receivedChar == 'B') {
      digitalWrite(pin4, HIGH);  // Pin 4'ü aktif hale getir
      digitalWrite(pin5, HIGH);  // Pin 5'i aktif hale getir
    } else if (receivedChar == 'C') {
      digitalWrite(pin4, LOW);   // Pin 4'ü kapat
      digitalWrite(pin5, LOW);   // Pin 5'i kapat
    }
  }
}

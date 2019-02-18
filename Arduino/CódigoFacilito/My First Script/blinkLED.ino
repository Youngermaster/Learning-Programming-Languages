// Blink of a LED

void setup() {
    pinMode(13, OUTPUT);
}

void loop() {
    digitalwrite(13, HIGH);
    delay(1000);
    digitalwrite(13, LOW);
    delay(1000);
}
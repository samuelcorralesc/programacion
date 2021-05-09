
// parpadeo de Led

void setup() {
  pinMode(13, OUTPUT); //declarar el pin 13 como salida
}

void loop() {
 digitalWrite(13, HIGH); //Encendemos el led
 delay(10000); // espereamos 1 seg
 digitalWrite(13, LOW); // apagamos el led
 delay(10000); /// esperamos 1 seg 
}
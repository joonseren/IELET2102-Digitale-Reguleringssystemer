  // Arduino oving 1

// Define pins
#define PWM_PIN 9
#define CAPACITOR_PIN 1
#define POTMETER_PIN 0

// Definere variabler
float Kp = 0.1;
float Ki = 0.2;
float Kd = 1;

float e_prev = 0;
float e_prev2 = 0;
float u_prev = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PWM_PIN, OUTPUT);  
}

void loop() {
  // Read potentiometer ADC
  int potentiometer_ADC_level = analogRead(POTMETER_PIN);
  float potentiometer_voltage = (potentiometer_ADC_level/1023.0)*5.0;
  // int pwm_value = map(potentiometer_ADC_level, 0, 1023, 0, 255);

  // analogWrite(PWM_PIN, pwm_value);

  int capacitor_ADC_level = analogRead(CAPACITOR_PIN);
  float capacitor_voltage = (capacitor_ADC_level/1023.0)*5.0;

  // PID
  float err = potentiometer_voltage - capacitor_voltage;

  float u = u_prev + Kp*(err - e_prev) + Ki*err + Kd*(err - 2*e_prev + e_prev2);

  u = constrain(u, 0, 255);

  analogWrite(PWM_PIN, (int)u);

  e_prev = err;
  e_prev2 = e_prev;
  u_prev = u;

  
  // Write voltages to plotter (serial)
  Serial.print(capacitor_voltage);
  Serial.print(",");
  Serial.println(potentiometer_voltage);

  //delay(100);
}
#include <Arduino_FreeRTOS.h>
#include <semphr.h> 

#define INCLUDE_vTaskDelay 1

// Define pins
#define PWM_PIN 10
#define CAPACITOR_PIN 0
#define LED_GREEN_PIN 9
#define LED_RED_PIN 6

// Define constants
#define MAX_VOLTAGE 5.0
#define MIN_VOLTAGE 0.0
#define MAX_CHARGE_VOLTAGE 4.0
#define MIN_CHARGE_VOLTAGE 1.0
#define N_DAC_LEVELS 255
#define N_ADC_LEVELS 1023

volatile bool isCharging = true;
SemaphoreHandle_t chargeMutex;

// Task prototypes
void Task_LEDs( void *pvParameters);
void Task_Capacitor( void *pvParameters);

void setup() {
  
  // Now set up two tasks to run independently.
  xTaskCreate(
    Task_LEDs
    ,  "LEDs"   
    ,  128  // Stack size
    ,  NULL // Parameters
    ,  1 // priority
    ,  NULL ); // Task handle

  xTaskCreate(
    Task_Capacitor
    ,  "Capacitor"   
    ,  128  // Stack size
    ,  NULL // Parameters
    ,  1  // priority
    ,  NULL ); // Task handle

  Serial.begin(9600);
}

void loop() {
  // Empty
}

void Task_Capacitor(void *pvParameters)
{
  pinMode(PWM_PIN, OUTPUT);  

  const float adcToVoltage = MAX_VOLTAGE/N_ADC_LEVELS;


  while(true) // A Task shall never return or exit.
  {
    int adcLevel = analogRead(CAPACITOR_PIN);
    float voltage = adcLevel*adcToVoltage;

    if(isCharging) {
      analogWrite(PWM_PIN, 255);

      if(voltage >= MAX_CHARGE_VOLTAGE) {
        isCharging = false;
      }
    }
    else {
      analogWrite(PWM_PIN, 0);

      if(voltage <= MIN_CHARGE_VOLTAGE) {
        isCharging = true;
      }
    }
    Serial.print("Spenning over kondensator: ");
    Serial.print(voltage);
    Serial.println(" V");
  }
}

void Task_LEDs(void *pvParameters)
{
  pinMode(LED_GREEN_PIN, OUTPUT);  
  pinMode(LED_RED_PIN, OUTPUT);  

  // LED test
  digitalWrite(LED_GREEN_PIN, HIGH);  
  digitalWrite(LED_RED_PIN, HIGH);  

  while(true) // A Task shall never return or exit.
  {
    if(isCharging) {
      digitalWrite(LED_GREEN_PIN, HIGH);
      digitalWrite(LED_RED_PIN, LOW);
    } else {
      digitalWrite(LED_GREEN_PIN, LOW);
      digitalWrite(LED_RED_PIN, HIGH);

    }
  }
}

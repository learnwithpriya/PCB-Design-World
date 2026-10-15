/*
 * 6-Axis ESP32 Servo Robot Controller
 * Author: Priya Saraswat
 *
 * Hardware:
 * - ESP32 Dev Module
 * - PCA9685 16-channel PWM driver
 * - 6 servo motors on channels 0 to 5
 *
 * Libraries required:
 * - ESP32 Arduino core
 * - Adafruit PWM Servo Driver Library
 */

#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

const uint8_t AXIS_COUNT = 6;
const uint8_t servoChannel[AXIS_COUNT] = {0, 1, 2, 3, 4, 5};

const int8_t I2C_SDA = 21;
const int8_t I2C_SCL = 22;

const int SERVO_MIN_US = 500;
const int SERVO_MAX_US = 2500;
const int DEFAULT_ANGLE = 90;

const float PWM_FREQUENCY_HZ = 50.0;
const uint32_t PWM_TICKS_PER_CYCLE = 4096;
const uint32_t PWM_PERIOD_US = 20000;

int currentAngle[AXIS_COUNT];
String rxLine;

void setup() {
  Serial.begin(115200);
  delay(200);

  Wire.begin(I2C_SDA, I2C_SCL);

  pwm.begin();
  pwm.setPWMFreq(PWM_FREQUENCY_HZ);

  for (uint8_t i = 0; i < AXIS_COUNT; i++) {
    currentAngle[i] = DEFAULT_ANGLE;
  }

  applyAllAngles();

  Serial.println();
  Serial.println("======================================");
  Serial.println(" 6-Axis ESP32 Servo Controller");
  Serial.println(" Author: Priya Saraswat");
  Serial.println("======================================");

  printHelp();
}

void loop() {
  while (Serial.available()) {
    char c = (char)Serial.read();

    if (c == '\n') {
      parseCommand(rxLine);
      rxLine = "";
    } else if (c != '\r') {
      rxLine += c;
    }
  }
}

void parseCommand(String raw) {
  raw.trim();
  raw.toUpperCase();

  if (raw.length() == 0) {
    return;
  }

  if (raw == "PING") {
    Serial.println("PONG");
  }
  else if (raw == "HELP") {
    printHelp();
  }
  else if (raw == "STATUS") {
    printStatus();
  }
  else if (raw == "CENTER") {
    centerAll();
    Serial.println("All axes centered at 90 degrees.");
  }
  else if (raw == "ZERO") {
    zeroAll();
    Serial.println("All axes moved to 0 degrees.");
  }
  else if (raw == "STOP") {
    centerAll();
    Serial.println("STOP command received. Servos moved to safe center position.");
    Serial.println("For real emergency stop, use hardware power cutoff or PCA9685 OE control.");
  }
  else if (raw.startsWith("MOVE ")) {
    parseMove(raw.substring(5));
  }
  else if (raw.startsWith("SET ")) {
    parseSet(raw.substring(4));
  }
  else {
    Serial.println("Unknown command. Type HELP for command list.");
  }
}

void parseMove(String args) {
  args.trim();

  int spaceIndex = args.indexOf(' ');

  if (spaceIndex < 0) {
    Serial.println("Format: MOVE <axis> <angle>");
    Serial.println("Example: MOVE 1 90");
    return;
  }

  int axis = args.substring(0, spaceIndex).toInt();
  int angle = args.substring(spaceIndex + 1).toInt();

  if (axis < 1 || axis > AXIS_COUNT) {
    Serial.println("Invalid axis. Use 1 to 6.");
    return;
  }

  setServoAngle(axis - 1, angle);

  Serial.print("Moved Axis ");
  Serial.print(axis);
  Serial.print(" to ");
  Serial.print(currentAngle[axis - 1]);
  Serial.println(" degrees.");
}

void parseSet(String args) {
  int values[AXIS_COUNT];
  int count = 0;
  String token;

  args += ' ';

  for (uint16_t i = 0; i < args.length(); i++) {
    char c = args[i];

    if (c == ' ') {
      if (token.length() > 0) {
        if (count < AXIS_COUNT) {
          values[count] = token.toInt();
        }
        count++;
        token = "";
      }
    } else {
      token += c;
    }
  }

  if (count != AXIS_COUNT) {
    Serial.println("Format: SET <a1> <a2> <a3> <a4> <a5> <a6>");
    Serial.println("Example: SET 0 45 90 135 90 45");
    return;
  }

  for (uint8_t i = 0; i < AXIS_COUNT; i++) {
    setServoAngle(i, values[i]);
  }

  Serial.println("All axes updated.");
  printStatus();
}

void setServoAngle(uint8_t axisIndex, int angleDegrees) {
  if (axisIndex >= AXIS_COUNT) {
    return;
  }

  angleDegrees = constrain(angleDegrees, 0, 180);

  int pulseUs = map(angleDegrees, 0, 180, SERVO_MIN_US, SERVO_MAX_US);

  uint32_t pulseTicks = (uint32_t)pulseUs * PWM_TICKS_PER_CYCLE / PWM_PERIOD_US;

  pwm.setPWM(servoChannel[axisIndex], 0, pulseTicks);

  currentAngle[axisIndex] = angleDegrees;
}

void applyAllAngles() {
  for (uint8_t i = 0; i < AXIS_COUNT; i++) {
    setServoAngle(i, currentAngle[i]);
  }
}

void centerAll() {
  for (uint8_t i = 0; i < AXIS_COUNT; i++) {
    setServoAngle(i, DEFAULT_ANGLE);
  }
}

void zeroAll() {
  for (uint8_t i = 0; i < AXIS_COUNT; i++) {
    setServoAngle(i, 0);
  }
}

void printStatus() {
  Serial.print("AXES:");

  for (uint8_t i = 0; i < AXIS_COUNT; i++) {
    Serial.print(' ');
    Serial.print(currentAngle[i]);
  }

  Serial.println();
}

void printHelp() {
  Serial.println("Available commands:");
  Serial.println("PING");
  Serial.println("HELP");
  Serial.println("STATUS");
  Serial.println("CENTER");
  Serial.println("ZERO");
  Serial.println("STOP");
  Serial.println("MOVE <axis> <angle>");
  Serial.println("SET <a1> <a2> <a3> <a4> <a5> <a6>");
  Serial.println();
  Serial.println("Examples:");
  Serial.println("MOVE 1 90");
  Serial.println("SET 0 45 90 135 90 45");
}

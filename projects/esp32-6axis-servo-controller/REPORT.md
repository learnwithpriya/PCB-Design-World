# Design and Development of a 6-Axis ESP32 Servo Robot Controller PCB

**Submitted by:**  
Priya Saraswat

**GitHub:**  
https://github.com/learnwithpriya

**Project Category:**  
Embedded Systems, Robotics, PCB Design

---

## Table of Contents

1. Abstract  
2. Introduction  
3. Objectives  
4. System Requirements  
5. Proposed Architecture  
6. Hardware Design  
7. Block Diagram  
8. Circuit Explanation  
9. Power Supply Design  
10. Servo Motor Selection  
11. PCA9685 Servo Driver  
12. ESP32 Microcontroller  
13. Communication Interface  
14. Firmware Design  
15. Serial Command Protocol  
16. PCB Design Considerations  
17. Safety Features  
18. Testing Plan  
19. Expected Results  
20. Limitations  
21. Future Improvements  
22. Conclusion  
23. References  

---

## 1. Abstract

This project presents the design of a controller PCB for a six-axis robotic arm. The system uses an ESP32 microcontroller as the main processing unit and a PCA9685 16-channel PWM driver to generate control signals for six servo motors. The controller accepts motion commands through a USB serial interface and provides a simple command protocol for testing individual axes or setting all axes simultaneously.

The design focuses on easy integration, modular construction, stable servo control, and safe power distribution. A separate servo power rail is used to prevent voltage drops and reset issues caused by motor current spikes.

---

## 2. Introduction

A six-axis robot, also called a six-degree-of-freedom robot, uses six joint actuators to move in multiple directions. For low-cost and educational robotic arms, servo motors are commonly used because they provide position control using a simple PWM signal.

The controller PCB must receive commands, process motion instructions, generate accurate PWM signals, provide regulated power, support safety features, and allow debugging through serial messages.

This project implements a compact controller based on ESP32 and PCA9685.

---

## 3. Objectives

The main objectives are:

1. Design a 6-axis robot controller using ESP32.
2. Interface six servo motors using a PCA9685 PWM driver.
3. Develop firmware for serial command-based motion control.
4. Create a PCB-ready architecture with separate logic and servo power domains.
5. Include basic safety and debugging features.
6. Document the complete design process for portfolio or freelancing use.

---

## 4. System Requirements

### Input Requirements

- USB connection for programming and serial commands
- External servo power supply, typically 5V or 6V
- Logic supply, typically 3.3V
- Optional emergency stop input
- Optional limit switch inputs for advanced versions

### Output Requirements

- Six PWM output channels for servo motors
- Status LED output
- Serial debug output
- Optional relay or MOSFET control for servo power enable

### Performance Requirements

- Stable 50 Hz PWM signals
- Servo pulse width support from approximately 500 us to 2500 us
- Serial commands at 115200 baud
- Invalid axis and angle protection
- Common ground between logic and motor sections

---

## 5. Proposed Architecture

Signal architecture:

```text
USB Host / Serial Terminal
        |
        v
      ESP32
        |
        v
     PCA9685
        |
        v
Six Servo Motors
```

Power architecture:

```text
DC Input / USB 5V
        |
        +--> 5V/6V Servo Rail --> PCA9685 V+ --> Servo Motors
        |
        +--> 3.3V Logic Rail --> ESP32 and PCA9685 VDD
```

This separation is important because servo motors can cause large current spikes.

---

## 6. Hardware Design

The hardware consists of four major blocks:

1. ESP32 controller section
2. PCA9685 PWM driver section
3. Servo output connector section
4. Power regulation section

---

## 7. Block Diagram

The block diagram is included in:

```text
docs/block_diagram.svg
```

It shows:

- USB/serial host
- ESP32 controller
- PCA9685 driver
- Six servo axes
- Power input
- 3.3V logic rail
- 5V/6V servo rail
- Emergency stop / safety input
- Status LEDs

---

## 8. Circuit Explanation

### ESP32 to PCA9685 Connection

The ESP32 communicates with the PCA9685 using I2C.

| ESP32 Pin | PCA9685 Pin | Description |
|---|---|---|
| GPIO21 | SDA | I2C data |
| GPIO22 | SCL | I2C clock |
| 3.3V | VDD | Logic supply |
| GND | GND | Common ground |

The SDA and SCL lines require pull-up resistors, typically 4.7 kOhm to 3.3V.

### PCA9685 Servo Output

The PCA9685 provides 16 PWM channels. Channels 0 to 5 are used for the six robot axes.

| PCA9685 Channel | Robot Axis |
|---|---|
| CH0 | Axis 1 |
| CH1 | Axis 2 |
| CH2 | Axis 3 |
| CH3 | Axis 4 |
| CH4 | Axis 5 |
| CH5 | Axis 6 |

Each servo connector has three pins:

```text
Signal
V+
GND
```

### Output Enable

The PCA9685 has an Output Enable pin, labeled OE. This pin is active low.

For normal operation:

```text
OE connected to GND
```

For advanced safety design:

```text
OE can be controlled by ESP32 GPIO or emergency stop circuit
```

---

## 9. Power Supply Design

### Logic Supply

The ESP32 and PCA9685 VDD require 3.3V.

Options:

- ESP32 Dev Module 3.3V pin for low-current testing
- AMS1117-3.3 LDO for simple PCB design
- MP1584 or similar buck converter for better efficiency

### Servo Supply

Servo motors require higher current.

For MG996R-type servos:

```text
Recommended voltage: 5V to 6.5V
Recommended current: 5A to 10A for six servos
```

For DS3218-type servos:

```text
Recommended voltage: 6V to 7.4V
Recommended current: depends on load and stall current
```

A separate 5V/6V supply should be used for the servo rail.

### Common Ground

The following grounds must be connected:

- ESP32 GND
- PCA9685 GND
- Servo supply GND
- USB ground if using USB communication

Without common ground, PWM signals will not have a valid reference and servos may jitter or not move.

### Filtering

Recommended filtering:

- 100 nF ceramic capacitor near PCA9685 VDD
- 100 nF ceramic capacitor near each servo connector or driver section
- 470 uF to 1000 uF electrolytic capacitor on servo power rail
- Optional TVS diode or reverse polarity protection on DC input

---

## 10. Servo Motor Selection

Standard hobby servos use a 50 Hz PWM signal.

Typical pulse ranges:

```text
0 degrees   = 1000 us or 500 us depending on servo
90 degrees  = 1500 us
180 degrees = 2000 us or 2500 us depending on servo
```

For this project, the firmware uses:

```text
SERVO_MIN_US = 500
SERVO_MAX_US = 2500
```

Recommended servos:

| Servo | Voltage | Use Case |
|---|---|---|
| SG90 | 4.8V to 6V | Very light prototype |
| MG996R | 5V to 6.5V | Medium robotic arm |
| DS3218 | 6V to 7.4V | Higher torque arm |
| FY3218SG | 6V to 7.4V | Strong hobby servo |

For a freelancing demo, MG996R or DS3218 is a practical choice.

---

## 11. PCA9685 Servo Driver

The PCA9685 is a 16-channel PWM driver controlled using I2C.

Important features:

- Supports 50 Hz PWM
- Programmable resolution up to 12 bits
- Reduces GPIO requirement
- Provides clean servo signals
- Can drive more than six servos if future expansion is needed

Default I2C address:

```text
0x40
```

Address can be changed using A0 to A5 pins.

---

## 12. ESP32 Microcontroller

The ESP32 is selected because it provides:

- USB serial communication
- I2C interface
- Wi-Fi and Bluetooth for future expansion
- Enough GPIO for buttons, LEDs, and sensors
- Low cost and wide availability

For this project, the ESP32 performs:

- Serial command parsing
- Angle validation
- I2C communication with PCA9685
- Status reporting
- Optional safety handling

---

## 13. Communication Interface

The controller uses USB serial communication.

Default settings:

```text
Baud rate: 115200
Data bits: 8
Parity: None
Stop bits: 1
```

The host computer can send commands using:

- Arduino Serial Monitor
- PuTTY
- Tera Term
- Python script
- Node-RED
- Mobile app through Bluetooth/Wi-Fi in future version

---

## 14. Firmware Design

The firmware is written for Arduino IDE using the ESP32 board package.

Main modules:

1. Serial input handler
2. Command parser
3. Servo angle mapper
4. PCA9685 PWM writer
5. Status reporter

Firmware flow:

```text
Start
  |
  v
Initialize Serial
  |
  v
Initialize I2C
  |
  v
Initialize PCA9685
  |
  v
Set all servos to center
  |
  v
Wait for serial command
  |
  v
Parse command
```

---

## 15. Serial Command Protocol

### PING

Request:

```text
PING
```

Response:

```text
PONG
```

### HELP

Request:

```text
HELP
```

Response:

```text
Available commands:
PING
HELP
STATUS
CENTER
ZERO
STOP
MOVE <axis> <angle>
SET <a1> <a2> <a3> <a4> <a5> <a6>
```

### STATUS

Request:

```text
STATUS
```

Response:

```text
AXES: 90 90 90 90 90 90
```

### MOVE

Request:

```text
MOVE 1 45
```

Meaning:

```text
Move Axis 1 to 45 degrees
```

Valid axis range:

```text
1 to 6
```

Valid angle range:

```text
0 to 180 degrees
```

### SET

Request:

```text
SET 0 30 60 90 120 150
```

Meaning:

```text
Axis 1 = 0
Axis 2 = 30
Axis 3 = 60
Axis 4 = 90
Axis 5 = 120
Axis 6 = 150
```

### CENTER

Request:

```text
CENTER
```

Meaning:

```text
All axes move to 90 degrees
```

### ZERO

Request:

```text
ZERO
```

Meaning:

```text
All axes move to 0 degrees
```

### STOP

Request:

```text
STOP
```

Meaning:

```text
All axes move to safe center position
```

For a real emergency stop, hardware power cutoff should be used.

---

## 16. PCB Design Considerations

The PCB should separate:

- Logic power
- Servo power
- Signal traces
- Ground return paths

Important rules:

1. Keep servo power traces wide.
2. Place decoupling capacitors close to ICs.
3. Do not route servo power through thin ESP32 pins.
4. Use screw terminals or JST connectors for servos.
5. Add clear silkscreen labels for Axis 1 to Axis 6.
6. Add test points for 3.3V, 5V, GND, SDA, SCL, and serial TX/RX.
7. Keep ESP32 antenna area free of copper and traces.
8. Add mounting holes at corners.
9. Provide polarity marking for DC input.
10. Add optional fuse holder on servo supply.

---

## 17. Safety Features

Recommended safety features:

### Emergency Stop

An emergency stop button can cut servo power using:

- Relay
- MOSFET high-side switch
- PCA9685 OE control
- Physical power switch

### Reverse Polarity Protection

Use:

- Schottky diode
- P-channel MOSFET
- DC jack with center-positive polarity marking

### Overcurrent Protection

Use:

- Polyfuse
- Inline fuse
- Current-limiting DC-DC module

### Brownout Prevention

Use:

- Bulk capacitor on servo rail
- Separate logic regulator
- Short and thick power traces

---

## 18. Testing Plan

### Test 1: Power Rail Test

Measure:

```text
Logic rail: 3.3V +/- 0.2V
Servo rail: 5V or 6V depending on servo
```

Check:

- No short circuit
- Correct polarity
- Stable voltage under servo movement

### Test 2: I2C Communication Test

Confirm PCA9685 is reachable.

Expected:

```text
ESP32 communicates with PCA9685 at address 0x40
```

### Test 3: Single Servo Test

Connect one servo to channel 0.

Send:

```text
MOVE 1 0
MOVE 1 90
MOVE 1 180
```

Observe:

- Servo moves smoothly
- No excessive jitter
- No ESP32 reset

### Test 4: Six Axis Test

Connect all six servos.

Send:

```text
SET 0 0 0 0 0 0
SET 90 90 90 90 90 90
SET 180 180 180 180 180 180
```

Observe:

- All axes respond correctly
- Axis numbering matches physical robot arm
- Power supply remains stable

### Test 5: Command Validation Test

Send invalid commands:

```text
MOVE 7 90
MOVE 1 200
HELPP
```

Expected:

- Firmware rejects invalid axis
- Firmware clamps invalid angle
- Unknown command prints error

---

## 19. Expected Results

After successful implementation, the system should:

- Turn on ESP32 and communicate over USB serial
- Detect PCA9685 on I2C bus
- Move all six servos using serial commands
- Maintain stable power during motion
- Respond to STATUS command with current axis angles
- Provide a repeatable platform for robotic arm control

Actual measured results should be recorded during hardware testing and added to this report.

---

## 20. Limitations

Current version limitations:

- Uses servo motors, not high-precision stepper motors
- No closed-loop position feedback
- No encoder integration
- Basic firmware does not include trajectory planning
- Emergency stop is recommended but may require hardware addition
- Servo range is limited by mechanical arm design

---

## 21. Future Improvements

Possible improvements:

1. Add Wi-Fi control using ESP32 built-in wireless.
2. Add Bluetooth joystick control.
3. Add OLED display for status.
4. Add current sensing for each servo.
5. Add limit switches for hard stops.
6. Add EEPROM storage for home positions.
7. Add inverse kinematics for Cartesian control.
8. Replace servos with stepper motors for higher precision.
9. Add CAN bus or RS-485 for industrial communication.
10. Create a mobile app or web dashboard.

---

## 22. Conclusion

This project demonstrates a practical 6-axis robot controller using ESP32 and PCA9685. The design is simple, modular, and suitable for educational robotics or freelance prototyping. By separating logic and servo power domains and using a serial command protocol, the controller becomes easy to test and expand.

The firmware provides basic motion control for six axes, while the hardware design allows future additions such as emergency stop, limit switches, wireless control, and sensor feedback.

This project can serve as a strong portfolio item for embedded systems, PCB design, and robotics.

---

## 23. References

1. Espressif Systems, ESP32 Series Datasheet.  
2. NXP Semiconductors, PCA9685 16-channel PWM-FMBUS LED Driver Datasheet.  
3. Adafruit PWM Servo Driver Library documentation.  
4. General servo motor PWM timing guidelines.  
5. Public robotics controller examples were reviewed only for general architecture inspiration. This repository contains an original ESP32 + PCA9685 implementation and documentation by Priya Saraswat.

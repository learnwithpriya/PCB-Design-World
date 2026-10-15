from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
PROJECT_DIR = Path("projects/esp32-6axis-servo-controller")
ASSETS_DIR = Path("assets")

ROOT_PROJECT_SECTION = r"""
### 1. 6-Axis ESP32 Servo Robot Controller

![6-Axis ESP32 Servo Robot Controller Banner](projects/esp32-6axis-servo-controller/docs/banner.svg)

An original 6-axis robot controller project using ESP32 and PCA9685 PWM driver. Designed to control six servo motors for a robotic arm prototype.

**Tech:** ESP32, PCA9685, Servo Motors, I2C, Arduino Framework, PCB Design Documentation

**Project Folder:** [projects/esp32-6axis-servo-controller](projects/esp32-6axis-servo-controller)

**Full Report:** [REPORT.md](projects/esp32-6axis-servo-controller/REPORT.md)

**Firmware:** [esp32_6axis_servo_controller.ino](projects/esp32-6axis-servo-controller/firmware/esp32_6axis_servo_controller/esp32_6axis_servo_controller.ino)

**BOM:** [BOM.csv](projects/esp32-6axis-servo-controller/hardware/BOM.csv)

**PCB Checklist:** [pcb_checklist.md](projects/esp32-6axis-servo-controller/hardware/pcb_checklist.md)
"""

FILES = {}

FILES[str(PROJECT_DIR / "README.md")] = r"""
# 6-Axis ESP32 Servo Robot Controller

![Banner](docs/banner.svg)

**Author:** Priya Saraswat  
**GitHub:** https://github.com/learnwithpriya  
**Project Type:** Embedded Systems / Robotics / PCB Design

This project is an original 6-axis robot controller design using ESP32 and PCA9685 PWM driver. It controls six servo motors for a robotic arm prototype.

---

## Features

- ESP32-based controller
- PCA9685 16-channel PWM servo driver
- Six servo motor output channels
- USB serial command interface
- Adjustable servo pulse width range
- Status reporting through serial monitor
- Modular PCB-friendly architecture
- Suitable for educational robotics and freelance prototype work

---

## Block Diagram

```mermaid
flowchart LR
    A[USB / Serial Host] --> B[ESP32 Controller]
    B --> C[PCA9685 PWM Driver]
    C --> D1[Axis 1 Servo]
    C --> D2[Axis 2 Servo]
    C --> D3[Axis 3 Servo]
    C --> D4[Axis 4 Servo]
    C --> D5[Axis 5 Servo]
    C --> D6[Axis 6 Servo]

    E[5V / 6V Servo Supply] --> C
    F[3.3V Logic Supply] --> B
    F --> C
    G[E-Stop / Safety Input] --> B
    B --> H[Status LEDs]
```

---

## Images

### Block Diagram SVG

![Block Diagram](docs/block_diagram.svg)

### Wiring Diagram SVG

![Wiring Diagram](docs/wiring_diagram.svg)

### Power Tree SVG

![Power Tree](docs/power_tree.svg)

---

## Hardware Used

| Component | Quantity | Purpose |
|---|---:|---|
| ESP32 Dev Module | 1 | Main controller |
| PCA9685 PWM Driver | 1 | Servo signal generation |
| Servo Motor | 6 | Axis 1 to Axis 6 |
| 5V/6V Power Supply | 1 | Servo power |
| 3.3V Regulator | 1 | Logic power |
| 4.7k Resistors | 2 | I2C pull-ups |
| 100nF Capacitors | Multiple | Decoupling |
| 470uF Capacitor | 1 | Servo rail filtering |
| Servo Connectors | 6 | Motor output |
| DC Power Jack | 1 | Power input |
| Status LED | 1 | Debug indication |

---

## Firmware

Firmware file:

```text
firmware/esp32_6axis_servo_controller/esp32_6axis_servo_controller.ino
```

Required Arduino libraries:

1. ESP32 Board Package
2. Adafruit PWM Servo Driver Library

Board settings:

```text
Board: ESP32 Dev Module
Baud Rate: 115200
```

---

## Serial Commands

Open Serial Monitor at:

```text
115200 baud
```

Commands:

```text
PING
HELP
STATUS
CENTER
ZERO
STOP
MOVE <axis> <angle>
SET <a1> <a2> <a3> <a4> <a5> <a6>
```

Examples:

```text
PING
```

Response:

```text
PONG
```

Move Axis 1 to 90 degrees:

```text
MOVE 1 90
```

Set all axes:

```text
SET 0 45 90 135 90 45
```

Center all axes:

```text
CENTER
```

Safe stop:

```text
STOP
```

---

## Important Power Warning

Do not power six servo motors directly from the ESP32 USB port or ESP32 5V pin.

Use:

- Separate 5V/6V servo supply
- Common ground between ESP32, PCA9685, and servo supply
- Bulk capacitor on servo power rail
- Fuse or current limiting for demo/freelance use

---

## Folder Structure

```text
/docs       Documentation and diagrams
/firmware   ESP32 firmware source code
/hardware   BOM and PCB checklist
README.md   Project overview
REPORT.md   Full project report
```

---

## Attribution

This project was developed as an original ESP32 + PCA9685 servo controller design. Public robotics controller examples were used only as general background reference. The architecture, documentation, firmware structure, and PCB design checklist in this repository are my own work unless otherwise credited.

**Designed and documented by Priya Saraswat.**
"""

FILES[str(PROJECT_DIR / "REPORT.md")] = r"""
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
"""

FILES[str(PROJECT_DIR / "docs/circuit_explanation.md")] = r"""
# Circuit Explanation

## Main Blocks

The circuit has four main blocks:

1. ESP32 controller
2. PCA9685 PWM driver
3. Servo output connectors
4. Power supply section

---

## ESP32 to PCA9685

The ESP32 controls the PCA9685 using I2C.

| ESP32 | PCA9685 |
|---|---|
| GPIO21 | SDA |
| GPIO22 | SCL |
| 3.3V | VDD |
| GND | GND |

Add 4.7 kOhm pull-up resistors from SDA to 3.3V and SCL to 3.3V.

---

## PCA9685 Power Pins

| Pin | Connection |
|---|---|
| VDD | 3.3V logic supply |
| V+ | 5V/6V servo supply |
| GND | Common ground |
| OE | GND for normal operation |

---

## Servo Connections

Each servo has three wires:

| Servo Wire | Connection |
|---|---|
| Signal | PCA9685 channel output |
| Positive | Servo V+ rail |
| Negative | Common GND |

Use channels 0 to 5 for Axis 1 to Axis 6.

---

## Power Recommendation

For testing:

```text
ESP32 powered by USB
PCA9685 VDD from ESP32 3.3V
Servo V+ from external 5V/6V supply
All GND connected together
```

For PCB:

```text
DC input -> Buck converter -> 5V/6V servo rail
DC input or 5V -> 3.3V regulator -> ESP32 and PCA9685 VDD
```

---

## Important Ground Rule

All grounds must be common:

```text
ESP32 GND = PCA9685 GND = Servo Supply GND
```

If grounds are not common, servos may jitter or not respond.

---

## Noise Reduction

Add:

- 100 nF ceramic capacitor near PCA9685 VDD
- 100 nF capacitor near servo power input
- 470 uF or 1000 uF electrolytic capacitor on servo rail
- Short and wide traces for servo power
"""

FILES[str(PROJECT_DIR / "docs/user_manual.md")] = r"""
# User Manual

## 1. Power Connection

Connect a suitable servo power supply to the board.

Recommended:

```text
5V to 6V DC for MG996R servos
6V to 7.4V DC for DS3218 servos
```

Ensure polarity is correct.

---

## 2. USB Connection

Connect ESP32 to computer using USB cable.

Open Serial Monitor at:

```text
115200 baud
```

---

## 3. Test Communication

Send:

```text
PING
```

Expected response:

```text
PONG
```

---

## 4. Move One Axis

Send:

```text
MOVE 1 90
```

This moves Axis 1 to 90 degrees.

---

## 5. Move All Axes

Send:

```text
SET 0 45 90 135 90 45
```

This sets:

```text
Axis 1 = 0
Axis 2 = 45
Axis 3 = 90
Axis 4 = 135
Axis 5 = 90
Axis 6 = 45
```

---

## 6. Center All Axes

Send:

```text
CENTER
```

All axes move to 90 degrees.

---

## 7. Zero All Axes

Send:

```text
ZERO
```

All axes move to 0 degrees.

---

## 8. Safe Stop

Send:

```text
STOP
```

All axes move to safe center position.

For real emergency stop, use hardware power cutoff.

---

## 9. Calibration

If servo range is incorrect, modify these values in firmware:

```cpp
const int SERVO_MIN_US = 500;
const int SERVO_MAX_US = 2500;
```

Some servos use:

```text
1000 us to 2000 us
```

Others use:

```text
500 us to 2500 us
```

---

## 10. Troubleshooting

| Problem | Possible Cause | Solution |
|---|---|---|
| No serial response | Wrong COM port or baud rate | Check port and set 115200 |
| Servo jitter | Bad ground or noisy supply | Connect common GND, add capacitor |
| ESP32 resets | Servo current too high | Use separate servo supply |
| Servo does not move | Wrong channel or power | Check V+, GND, signal |
| Invalid angle | Angle out of range | Use 0 to 180 degrees |
"""

FILES[str(PROJECT_DIR / "docs/testing_report_template.md")] = r"""
# Testing Report Template

**Project:** 6-Axis ESP32 Servo Robot Controller  
**Author:** Priya Saraswat  
**Date:** ______________________  
**Tester:** ______________________  

---

## 1. Hardware Inspection

| Check | Result | Notes |
|---|---|---|
| No visible shorts | Pass / Fail | |
| Correct polarity | Pass / Fail | |
| Connectors secure | Pass / Fail | |
| ESP32 antenna clear | Pass / Fail | |
| Servo labels correct | Pass / Fail | |

---

## 2. Power Rail Tests

| Rail | Expected | Measured | Result |
|---|---:|---:|---|
| 3.3V Logic | 3.3V | ______ V | Pass / Fail |
| 5V/6V Servo | 5V or 6V | ______ V | Pass / Fail |
| GND continuity | 0 ohm | ______ ohm | Pass / Fail |

---

## 3. Communication Tests

| Test | Command | Expected | Result |
|---|---|---|---|
| Boot message | Power on | Banner appears | Pass / Fail |
| Ping | PING | PONG | Pass / Fail |
| Help | HELP | Command list | Pass / Fail |
| Status | STATUS | AXES values | Pass / Fail |

---

## 4. Servo Axis Tests

| Axis | Channel | MOVE 0 | MOVE 90 | MOVE 180 | Result |
|---|---:|---|---|---|---|
| Axis 1 | CH0 | Pass / Fail | Pass / Fail | Pass / Fail | |
| Axis 2 | CH1 | Pass / Fail | Pass / Fail | Pass / Fail | |
| Axis 3 | CH2 | Pass / Fail | Pass / Fail | Pass / Fail | |
| Axis 4 | CH3 | Pass / Fail | Pass / Fail | Pass / Fail | |
| Axis 5 | CH4 | Pass / Fail | Pass / Fail | Pass / Fail | |
| Axis 6 | CH5 | Pass / Fail | Pass / Fail | Pass / Fail | |

---

## 5. Load Test

| Test | Observation | Result |
|---|---|---|
| All servos move together | No reset / jitter / voltage drop | Pass / Fail |
| Servo rail voltage under load | ______ V | Pass / Fail |
| Temperature after 5 minutes | Normal / Warm / Hot | Pass / Fail |

---

## 6. Safety Test

| Test | Expected | Result |
|---|---|---|
| STOP command | Servos move to safe position | Pass / Fail |
| E-stop input, if implemented | Servo power disabled | Pass / Fail |
| Invalid command | Error message shown | Pass / Fail |

---

## 7. Final Remarks

```text
Write observations, failures, fixes, and final status here.
```

**Signature:** ______________________
"""

FILES[str(PROJECT_DIR / "hardware/BOM.csv")] = r"""
Item,Qty,Part,Purpose,Notes
1,1,ESP32 Dev Module or ESP32-WROOM-32,Main controller,Use 3.3V logic supply
2,1,PCA9685 PWM Driver IC/Module,6-axis servo PWM output,I2C address 0x40
3,6,MG996R or DS3218 servo,Robot arm axes,Choose based on torque requirement
4,1,5V/6V 8A to 10A power supply,Servo power,Do not power servos from ESP32 USB
5,1,3.3V regulator or buck converter,Logic power,AMS1117-3.3 or MP1584 adjustable
6,2,4.7k resistor,I2C pull-ups,For SDA and SCL
7,10,100nF ceramic capacitor,Decoupling,Near ICs and servo connectors
8,1,470uF to 1000uF electrolytic capacitor,Servo rail bulk filter,Check voltage rating
9,6,3-pin servo connector or terminal,Servo output,Label Axis 1 to Axis 6
10,1,DC power jack or screw terminal,Power input,Add polarity marking
11,1,Push button,E-stop or reset,Optional
12,1,LED + resistor,Status indicator,Optional
13,1,PCB,Controller board,Design in KiCad/EasyEDA/JLCPCB
14,1,Fuse holder or polyfuse,Overcurrent protection,Recommended
15,1,Reverse polarity diode or PFET,Polarity protection,Recommended
"""

FILES[str(PROJECT_DIR / "hardware/pcb_checklist.md")] = r"""
# PCB Checklist for 6-Axis ESP32 Servo Controller

## 1. Schematic Checklist

- [ ] ESP32 power pins correctly connected
- [ ] PCA9685 VDD connected to 3.3V
- [ ] PCA9685 V+ connected to servo rail
- [ ] PCA9685 OE connected to GND or control GPIO
- [ ] I2C SDA and SCL have 4.7 kOhm pull-ups to 3.3V
- [ ] Six servo output connectors labeled Axis 1 to Axis 6
- [ ] Common ground between ESP32, PCA9685, and servo supply
- [ ] Decoupling capacitors added near ICs
- [ ] Bulk capacitor added on servo rail
- [ ] DC input polarity protection added
- [ ] Fuse or polyfuse added on servo power input
- [ ] Status LED and resistor added
- [ ] Test points added for UART, I2C, 3.3V, 5V/6V, GND

---

## 2. Power Checklist

- [ ] Logic rail is 3.3V
- [ ] Servo rail is 5V/6V or 6V/7.4V depending on servo
- [ ] Servo supply current rating is sufficient
- [ ] ESP32 is not powering servos directly
- [ ] Ground star or solid ground plane used
- [ ] Servo power traces are wide and short
- [ ] Input capacitor placed near DC jack
- [ ] Reverse polarity protection verified
- [ ] Fuse rating selected based on servo stall current

---

## 3. Layout Checklist

- [ ] ESP32 antenna keep-out area has no copper
- [ ] No traces under ESP32 antenna
- [ ] I2C traces are short
- [ ] Servo signal traces separated from high-current power traces
- [ ] Decoupling capacitors close to IC power pins
- [ ] Ground return path is continuous
- [ ] Mounting holes placed at corners
- [ ] Connector orientation is mechanically convenient
- [ ] Silkscreen labels are readable
- [ ] Polarity markings added for DC input and servos

---

## 4. Trace Width Guidance

For signal traces:

```text
10 to 12 mil is usually enough
```

For servo power traces:

```text
Use wide traces or copper pour.
For 5A to 10A, use 2oz copper or external power wires.
```

---

## 5. Assembly Checklist

- [ ] Check for shorts before applying power
- [ ] Measure 3.3V before connecting ESP32
- [ ] Measure servo rail before connecting servos
- [ ] Connect common ground first
- [ ] Test one servo before connecting all six
- [ ] Verify axis numbering matches robot arm
- [ ] Secure servo wires with strain relief
- [ ] Label all connectors clearly

---

## 6. Debug Checklist

- [ ] ESP32 boots normally
- [ ] Serial monitor responds to PING
- [ ] PCA9685 I2C address detected
- [ ] Servo moves on MOVE command
- [ ] No reset when servo starts moving
- [ ] No excessive jitter
- [ ] Power rail voltage stays stable under load
"""

FILES[str(PROJECT_DIR / "firmware/esp32_6axis_servo_controller/esp32_6axis_servo_controller.ino")] = r"""
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
"""

FILES[str(PROJECT_DIR / "docs/banner.svg")] = r"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">
  <rect width="1200" height="320" fill="#0f172a"/>
  <rect x="40" y="40" width="1120" height="240" rx="20" fill="#111827" stroke="#38bdf8" stroke-width="3"/>
  <text x="80" y="105" font-family="Arial, sans-serif" font-size="42" font-weight="bold" fill="#f8fafc">PCB Design World</text>
  <text x="80" y="155" font-family="Arial, sans-serif" font-size="30" fill="#38bdf8">6-Axis ESP32 Servo Robot Controller</text>
  <text x="80" y="205" font-family="Arial, sans-serif" font-size="22" fill="#e2e8f0">Designed &amp; documented by Priya Saraswat</text>
  <text x="80" y="245" font-family="Arial, sans-serif" font-size="18" fill="#94a3b8">Embedded Systems | Robotics | PCB Design | Portfolio Project</text>
</svg>
"""

FILES[str(PROJECT_DIR / "docs/block_diagram.svg")] = r"""
<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="700" viewBox="0 0 1100 700">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333333"/>
    </marker>
  </defs>

  <style>
    .title { font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: #111111; }
    .author { font-family: Arial, sans-serif; font-size: 16px; fill: #444444; }
    .box { fill: #ffffff; stroke: #333333; stroke-width: 2; }
    .smallbox { fill: #f7f7f7; stroke: #333333; stroke-width: 2; }
    .label { font-family: Arial, sans-serif; font-size: 14px; fill: #111111; text-anchor: middle; dominant-baseline: middle; }
    .line { stroke: #333333; stroke-width: 2; fill: none; marker-end: url(#arrow); }
  </style>

  <rect width="1100" height="700" fill="#ffffff"/>

  <text x="550" y="40" class="title" text-anchor="middle">6-Axis ESP32 Servo Controller Block Diagram</text>
  <text x="550" y="65" class="author" text-anchor="middle">Priya Saraswat</text>

  <rect x="40" y="120" width="170" height="70" rx="10" ry="10" class="box"/>
  <text x="125" y="155" class="label">USB / Serial Host</text>

  <rect x="310" y="110" width="190" height="90" rx="10" ry="10" class="box"/>
  <text x="405" y="145" class="label">ESP32</text>
  <text x="405" y="165" class="label">Command Parser</text>

  <rect x="40" y="280" width="170" height="70" rx="10" ry="10" class="box"/>
  <text x="125" y="315" class="label">5V / 12V DC Input</text>

  <rect x="310" y="260" width="190" height="50" rx="10" ry="10" class="box"/>
  <text x="405" y="285" class="label">5V / 6V Servo Rail</text>

  <rect x="310" y="330" width="190" height="50" rx="10" ry="10" class="box"/>
  <text x="405" y="355" class="label">3.3V Logic Rail</text>

  <rect x="610" y="150" width="180" height="110" rx="10" ry="10" class="box"/>
  <text x="700" y="190" class="label">PCA9685</text>
  <text x="700" y="210" class="label">16-Channel PWM</text>
  <text x="700" y="230" class="label">I2C Driver</text>

  <rect x="870" y="90" width="150" height="38" rx="8" ry="8" class="smallbox"/>
  <text x="945" y="109" class="label">Axis 1 Servo</text>

  <rect x="870" y="140" width="150" height="38" rx="8" ry="8" class="smallbox"/>
  <text x="945" y="159" class="label">Axis 2 Servo</text>

  <rect x="870" y="190" width="150" height="38" rx="8" ry="8" class="smallbox"/>
  <text x="945" y="209" class="label">Axis 3 Servo</text>

  <rect x="870" y="240" width="150" height="38" rx="8" ry="8" class="smallbox"/>
  <text x="945" y="259" class="label">Axis 4 Servo</text>

  <rect x="870" y="290" width="150" height="38" rx="8" ry="8" class="smallbox"/>
  <text x="945" y="309" class="label">Axis 5 Servo</text>

  <rect x="870" y="340" width="150" height="38" rx="8" ry="8" class="smallbox"/>
  <text x="945" y="359" class="label">Axis 6 Servo</text>

  <rect x="40" y="430" width="170" height="60" rx="10" ry="10" class="box"/>
  <text x="125" y="460" class="label">E-Stop / Safety Input</text>

  <rect x="310" y="430" width="190" height="60" rx="10" ry="10" class="box"/>
  <text x="405" y="460" class="label">Status LEDs</text>

  <path class="line" d="M210 155 L310 155"/>
  <path class="line" d="M210 315 L310 285"/>
  <path class="line" d="M210 315 L310 355"/>
  <path class="line" d="M405 330 L405 200"/>
  <path class="line" d="M500 285 L610 210"/>
  <path class="line" d="M500 155 L610 180"/>

  <path class="line" d="M790 180 L870 109"/>
  <path class="line" d="M790 190 L870 159"/>
  <path class="line" d="M790 200 L870 209"/>
  <path class="line" d="M790 210 L870 259"/>
  <path class="line" d="M790 220 L870 309"/>
  <path class="line" d="M790 230 L870 359"/>

  <path class="line" d="M125 430 L125 200 L310 180"/>
  <path class="line" d="M500 180 L405 430"/>

  <text x="550" y="650" class="author" text-anchor="middle">Copyright Priya Saraswat - Original Block Diagram</text>
</svg>
"""

FILES[str(PROJECT_DIR / "docs/wiring_diagram.svg")] = r"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">
  <style>
    .title { font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: #111; }
    .author { font-family: Arial, sans-serif; font-size: 16px; fill: #444; }
    .box { fill: #fff; stroke: #333; stroke-width: 2; }
    .pin { font-family: monospace; font-size: 13px; fill: #111; }
    .power { stroke: #c0392b; stroke-width: 3; fill: none; }
    .ground { stroke: #111; stroke-width: 3; fill: none; }
    .signal { stroke: #2980b9; stroke-width: 2; fill: none; }
    .label { font-family: Arial, sans-serif; font-size: 14px; fill: #111; }
  </style>

  <rect width="1200" height="720" fill="#fff"/>
  <text x="600" y="40" class="title" text-anchor="middle">ESP32 + PCA9685 + 6 Servo Wiring Diagram</text>
  <text x="600" y="65" class="author" text-anchor="middle">Priya Saraswat</text>

  <rect x="80" y="120" width="220" height="220" rx="12" class="box"/>
  <text x="190" y="150" class="label" text-anchor="middle">ESP32</text>
  <text x="110" y="190" class="pin">3.3V</text>
  <text x="110" y="220" class="pin">GND</text>
  <text x="110" y="250" class="pin">GPIO21 / SDA</text>
  <text x="110" y="280" class="pin">GPIO22 / SCL</text>
  <text x="110" y="310" class="pin">USB Serial</text>

  <rect x="450" y="120" width="250" height="260" rx="12" class="box"/>
  <text x="575" y="150" class="label" text-anchor="middle">PCA9685</text>
  <text x="480" y="190" class="pin">VDD = 3.3V</text>
  <text x="480" y="220" class="pin">GND</text>
  <text x="480" y="250" class="pin">SDA</text>
  <text x="480" y="280" class="pin">SCL</text>
  <text x="480" y="310" class="pin">OE -> GND</text>
  <text x="480" y="340" class="pin">V+ = 5V/6V</text>

  <rect x="820" y="90" width="260" height="360" rx="12" class="box"/>
  <text x="950" y="120" class="label" text-anchor="middle">6 Servo Motors</text>
  <text x="850" y="160" class="pin">CH0 -> Axis 1</text>
  <text x="850" y="190" class="pin">CH1 -> Axis 2</text>
  <text x="850" y="220" class="pin">CH2 -> Axis 3</text>
  <text x="850" y="250" class="pin">CH3 -> Axis 4</text>
  <text x="850" y="280" class="pin">CH4 -> Axis 5</text>
  <text x="850" y="310" class="pin">CH5 -> Axis 6</text>
  <text x="850" y="350" class="pin">Each servo: Signal, V+, GND</text>

  <rect x="80" y="450" width="220" height="120" rx="12" class="box"/>
  <text x="190" y="480" class="label" text-anchor="middle">5V/6V Servo Supply</text>
  <text x="110" y="520" class="pin">+ V</text>
  <text x="110" y="545" class="pin">GND</text>

  <path class="signal" d="M300 250 L450 250"/>
  <path class="signal" d="M300 280 L450 280"/>
  <path class="power" d="M300 190 L450 190"/>
  <path class="ground" d="M300 220 L450 220"/>

  <path class="power" d="M300 520 L575 520 L575 380"/>
  <path class="ground" d="M300 545 L575 545 L575 380"/>

  <path class="signal" d="M700 200 L820 160"/>
  <path class="signal" d="M700 220 L820 190"/>
  <path class="signal" d="M700 240 L820 220"/>
  <path class="signal" d="M700 260 L820 250"/>
  <path class="signal" d="M700 280 L820 280"/>
  <path class="signal" d="M700 300 L820 310"/>

  <text x="600" y="650" class="author" text-anchor="middle">Note: Keep all GND connections common. Do not power servos from ESP32 pin.</text>
</svg>
"""

FILES[str(PROJECT_DIR / "docs/power_tree.svg")] = r"""
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600" viewBox="0 0 1000 600">
  <style>
    .title { font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: #111; }
    .author { font-family: Arial, sans-serif; font-size: 16px; fill: #444; }
    .box { fill: #fff; stroke: #333; stroke-width: 2; }
    .label { font-family: Arial, sans-serif; font-size: 14px; fill: #111; text-anchor: middle; dominant-baseline: middle; }
    .line { stroke: #333; stroke-width: 2; fill: none; }
    .power { stroke: #c0392b; stroke-width: 3; fill: none; }
  </style>

  <rect width="1000" height="600" fill="#fff"/>
  <text x="500" y="40" class="title" text-anchor="middle">Power Tree</text>
  <text x="500" y="65" class="author" text-anchor="middle">Priya Saraswat</text>

  <rect x="380" y="100" width="240" height="70" rx="10" class="box"/>
  <text x="500" y="135" class="label">DC Input / USB 5V</text>

  <rect x="150" y="240" width="240" height="70" rx="10" class="box"/>
  <text x="270" y="265" class="label">5V / 6V Servo Rail</text>
  <text x="270" y="285" class="label">High Current</text>

  <rect x="610" y="240" width="240" height="70" rx="10" class="box"/>
  <text x="730" y="265" class="label">3.3V Logic Rail</text>
  <text x="730" y="285" class="label">Low Current</text>

  <rect x="80" y="400" width="180" height="60" rx="10" class="box"/>
  <text x="170" y="430" class="label">Servo Motors</text>

  <rect x="300" y="400" width="180" height="60" rx="10" class="box"/>
  <text x="390" y="430" class="label">PCA9685 V+</text>

  <rect x="620" y="400" width="160" height="60" rx="10" class="box"/>
  <text x="700" y="430" class="label">ESP32</text>

  <rect x="820" y="400" width="120" height="60" rx="10" class="box"/>
  <text x="880" y="430" class="label">PCA9685 VDD</text>

  <path class="power" d="M430 170 L270 240"/>
  <path class="line" d="M570 170 L730 240"/>

  <path class="power" d="M220 310 L170 400"/>
  <path class="power" d="M320 310 L390 400"/>

  <path class="line" d="M680 310 L700 400"/>
  <path class="line" d="M780 310 L880 400"/>

  <text x="500" y="540" class="author" text-anchor="middle">Separate servo power from logic power. Use common ground.</text>
</svg>
"""

FILES[str(ASSETS_DIR / "profile_banner.svg")] = r"""
<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="500" viewBox="0 0 1500 500">
  <rect width="1500" height="500" fill="#0f172a"/>
  <rect x="60" y="70" width="1380" height="360" rx="28" fill="#111827" stroke="#38bdf8" stroke-width="4"/>
  <text x="120" y="170" font-family="Arial, sans-serif" font-size="58" font-weight="bold" fill="#f8fafc">Priya Saraswat</text>
  <text x="120" y="235" font-family="Arial, sans-serif" font-size="34" fill="#38bdf8">Electronics Engineer | PCB Design Engineer | Embedded Systems Enthusiast</text>
  <text x="120" y="300" font-family="Arial, sans-serif" font-size="26" fill="#e2e8f0">PCB Design World - documenting practical electronics, robotics, and embedded projects.</text>
  <text x="120" y="355" font-family="Arial, sans-serif" font-size="22" fill="#94a3b8">Skills: Altium Designer, KiCad, OrCAD, LTspice, Proteus, PSpice, Arduino, ESP32, Embedded C</text>
</svg>
"""

FILES[str(ASSETS_DIR / "avatar_priya_saraswat.svg")] = r"""
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">
  <circle cx="200" cy="200" r="190" fill="#0f172a" stroke="#38bdf8" stroke-width="10"/>
  <text x="200" y="215" font-family="Arial, sans-serif" font-size="120" font-weight="bold" fill="#f8fafc" text-anchor="middle">PS</text>
  <text x="200" y="300" font-family="Arial, sans-serif" font-size="28" fill="#38bdf8" text-anchor="middle">Priya Saraswat</text>
  <text x="200" y="335" font-family="Arial, sans-serif" font-size="18" fill="#e2e8f0" text-anchor="middle">PCB Design World</text>
</svg>
"""

FILES[str(PROJECT_DIR / "images/.gitkeep")] = ""


def write_files():
    for rel_path, content in FILES.items():
        file_path = REPO_ROOT / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content.lstrip("\n"))

    print("Generated project files and images.")


def update_root_readme():
    readme_path = REPO_ROOT / "README.md"
    marker_start = "<!-- PORTFOLIO_PROJECTS_START -->"
    marker_end = "<!-- PORTFOLIO_PROJECTS_END -->"

    section_body = ROOT_PROJECT_SECTION.strip()
    new_block = f"\n{marker_start}\n\n{section_body}\n\n{marker_end}\n"

    if not readme_path.exists():
        base = "# PCB Design World\n\nElectronics, PCB design, embedded systems, and robotics projects by Priya Saraswat.\n"
        readme_path.write_text(base + new_block, encoding="utf-8")
        print("Created root README.md with featured projects section.")
        return

    text = readme_path.read_text(encoding="utf-8")

    if marker_start in text and marker_end in text:
        start_idx = text.index(marker_start)
        end_idx = text.index(marker_end) + len(marker_end)
        updated = text[:start_idx] + new_block.strip() + text[end_idx:]
    elif marker_start in text:
        updated = text + "\n" + section_body + "\n" + marker_end + "\n"
    else:
        updated = text.rstrip() + "\n" + new_block

    readme_path.write_text(updated, encoding="utf-8")
    print("Updated root README.md with featured projects section.")


def main():
    write_files()
    update_root_readme()

    print()
    print("Done.")
    print("Next steps:")
    print("1. Check generated files using: git status")
    print("2. Run: git add .")
    print("3. Run: git commit -m \"Add ESP32 6-axis servo controller project\"")
    print("4. Run: git push -u origin HEAD")


if __name__ == "__main__":
    main()
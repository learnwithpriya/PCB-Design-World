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

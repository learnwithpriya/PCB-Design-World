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

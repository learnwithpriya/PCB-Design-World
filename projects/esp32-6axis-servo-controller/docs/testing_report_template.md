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

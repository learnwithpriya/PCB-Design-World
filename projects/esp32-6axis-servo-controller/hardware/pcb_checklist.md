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

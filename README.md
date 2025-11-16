# Drowsiness Detection System (OpenCV + ESP32)

A real-time computer vision system that detects drowsiness using face & eye tracking, and triggers a **3-stage hardware alert** using an ESP32 board (LED → Buzzer → Vibration Motor).  
This project demonstrates practical end-to-end ML engineering: **real-time CV → decision logic → embedded hardware integration**.

---

##  Overview

This system uses:

- **OpenCV Haar Cascades** for face & eye detection  
- **Consecutive-frame heuristic** to detect prolonged eye closure  
- **Serial communication** to send alerts to ESP32  
- **Three-level hardware alert system**:  
  1️⃣ LED  
  2️⃣ LED + Buzzer  
  3️⃣ LED + Buzzer + Vibration  

Ideal for understanding real-time ML, CV pipelines, and embedded systems.

---

## 🧠 System Architecture


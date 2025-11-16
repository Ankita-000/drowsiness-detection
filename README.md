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
Camera Feed → OpenCV Face & Eye Detection → Drowsiness Logic (frames threshold)
↓
Serial Message (ALERT1 / ALERT2 / ALERT3)
↓
ESP32 Hardware Alerts
(LED → Buzzer → Vibration Motor depending on stage




---

## 📁 Project Structure

drowsiness-detection/
│── src/
│ ├── detection.py
│ ├── haarcascade_eye.xml
│ └── haarcascade_frontalface_default.xml
│
│── esp32/
│ └── alert_system.ino
│
│── assets/
│ ├── screenshots/
│ └── demo.mp4 (optional - add your demo video here)
│
└── requirements.txt




### **1. Install Dependencies**

pip install -r requirements.txt


### **2. Upload ESP32 Firmware**
Open esp32/alert_system.ino in Arduino IDE
Select your ESP32 board → Upload.



### **3. Run Detection Script**
   
python src/detection.py --serial_port COM6 --threshold 10

Examples of serial ports:
Windows: COM6
Linux: /dev/ttyUSB0
Mac: /dev/cu.usbserial*




##My Contributions

I built the full real-time detection pipeline using OpenCV (face + eye detection), created the drowsiness logic using consecutive-frame thresholding, implemented serial communication to ESP32, and wrote the ESP32 firmware to control LED, buzzer, and vibration motors. I designed and tested the complete 3-stage alert workflow and documented the project with a demo.



🔮 Future Improvements

*Replace Haar cascades with CNN-based eye state classifier
*Integrate YOLO or MediaPipe FaceMesh
*Deploy on Raspberry Pi / Jetson Nano
*Add a cloud dashboard for monitoring

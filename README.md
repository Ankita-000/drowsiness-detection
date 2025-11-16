
# Drowsiness Detection System (OpenCV + ESP32)

A real-time computer vision system that detects drowsiness using face & eye tracking, and triggers a 3-stage hardware alert using an ESP32 board (LED → Buzzer → Vibration Motor).
This project demonstrates practical end-to-end ML engineering: real-time CV → decision logic → embedded hardware integration.

## Overview

This system uses:
- OpenCV Haar Cascades for face & eye detection
- Consecutive-frame heuristic to detect prolonged eye closure
- Serial communication to send alerts to ESP32
- Three-level hardware alert system:
  1. LED
  2. LED + Buzzer
  3. LED + Buzzer + Vibration

Ideal for understanding real-time ML, CV pipelines, and embedded systems.

## System Architecture

Camera Feed → OpenCV Face & Eye Detection → Drowsiness Logic (frames threshold)
                     ↓
           Serial Message (ALERT1 / ALERT2 / ALERT3)
                     ↓
               ESP32 Hardware Alerts
     (LED → Buzzer → Vibration Motor depending on stage)

## Project Structure

drowsiness-detection/
  src/
    detection.py
    haarcascade_eye.xml
    haarcascade_frontalface_default.xml
  esp32/
    alert_system.ino
  assets/
    screenshots/
  requirements.txt

## Technologies Used

- Python 3
- OpenCV
- PySerial
- ESP32 / Arduino
- Pygame (optional)
- Webcam

## Installation & Setup

1. Install Dependencies:
   pip install -r requirements.txt

2. Upload ESP32 Firmware:
   Upload esp32/alert_system.ino through Arduino IDE.

3. Run Detection Script:
   python src/detection.py --serial_port COM6 --threshold 10

## My Contributions

I built the full real-time detection pipeline using OpenCV (face + eye detection), created the drowsiness logic using consecutive-frame thresholding, implemented serial communication to ESP32, and wrote the ESP32 firmware to control LED, buzzer, and vibration motors. I designed and tested the complete 3-stage alert workflow and documented the project.

## Future Improvements

- Replace Haar cascades with CNN-based eye state classifier
- Integrate YOLO or MediaPipe FaceMesh
- Deploy on Raspberry Pi / Jetson Nano
- Add a cloud dashboard for monitoring

## License
MIT License.





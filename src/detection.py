"""
detection.py
Real-time drowsiness detection using OpenCV Haar cascades + serial communication to ESP32.
"""

import cv2
import time
import argparse
import serial
import serial.tools.list_ports

# ---------------------------------------
# Auto-detect serial port (optional)
# ---------------------------------------
def find_serial_port():
    ports = serial.tools.list_ports.comports()
    return ports[0].device if ports else None


# ---------------------------------------
# ESP32 communication handler
# ---------------------------------------
class ESP32Controller:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        self.ser = None
        if port:
            try:
                self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
                time.sleep(2)  # wait for ESP to reboot
            except Exception as e:
                print(f"[WARNING] Could not connect to ESP32: {e}")

    def send(self, message):
        if not self.ser:
            return
        try:
            self.ser.write((message + "\n").encode())
        except:
            print("[WARNING] Failed to send data to ESP32")

    def close(self):
        if self.ser:
            self.ser.close()


# ---------------------------------------
# Main detection function
# ---------------------------------------
def main(args):
    # Load Haar Cascade Models
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # ESP32 Setup
    esp = None
    if args.serial_port:
        esp = ESP32Controller(args.serial_port)
    else:
        print("[INFO] Running WITHOUT ESP32 (no hardware alerts).")

    # Webcam Setup
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(" ERROR: Cannot access webcam")
        return

    closed_frames = 0
    stage = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        eyes_found = False

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)

            if len(eyes) > 0:
                eyes_found = True
                closed_frames = 0
                stage = 0

            break  # detect only first face

        if not eyes_found:
            closed_frames += 1

        # Alert Threshold Logic
        if closed_frames >= args.threshold and stage < 1:
            stage = 1
            print("[ALERT 1] LED Flash")
            if esp: esp.send("ALERT1")

        if closed_frames >= args.threshold * 2 and stage < 2:
            stage = 2
            print("[ALERT 2] LED + Buzzer")
            if esp: esp.send("ALERT2")

        if closed_frames >= args.threshold * 3 and stage < 3:
            stage = 3
            print("[ALERT 3] LED + Buzzer + Vibration")
            if esp: esp.send("ALERT3")

        # Display
        cv2.putText(frame, f"Closed Frames: {closed_frames}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        cv2.imshow("Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if esp:
        esp.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serial_port", type=str, default=None,
                        help="ESP32 serial port (COM6, /dev/ttyUSB0, etc.)")
    parser.add_argument("--threshold", type=int, default=10,
                        help="Frames required to trigger alert stage 1")
    args = parser.parse_args()

    main(args)

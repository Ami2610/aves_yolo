from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Cargar modelo
model = YOLO("best.pt")

# Cámara
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # YOLO inference
            results = model(frame)
            annotated_frame = results[0].plot()

            # Convertir a JPEG
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

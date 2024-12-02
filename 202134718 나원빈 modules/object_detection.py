import cv2

def detect_objects(image):
    # OpenCV를 사용하여 객체 탐지
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_objects = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        detected_objects.append(image[y:y+h, x:x+w])

    return detected_objects

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

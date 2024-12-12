import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 모델 불러오기
model = load_model('mask_detection_model.h5')  # 모델 파일 경로

# 얼굴 인식 위한 분류기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 파일 불러오기
image_path = 'images/image_01.jpg'  # 이미지 파일 경로
image = cv2.imread(image_path)

# 얼굴 검출
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 각 얼굴에 대해 마스크 여부 판단
for (x, y, w, h) in faces:
    roi = image[y:y+h, x:x+w]
    roi_resized = cv2.resize(roi, (224, 224))
    roi_resized = np.expand_dims(roi_resized, axis=0) / 255.0

    # 모델로 예측
    prediction = model.predict(roi_resized)
    label = 'Mask' if prediction[0][0] > 0.5 else 'No Mask'

    # 결과 표시
    color = (0, 255, 0) if label == 'Mask' else (0, 0, 255)
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

# 결과 이미지 출력
cv2.imshow('Mask Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

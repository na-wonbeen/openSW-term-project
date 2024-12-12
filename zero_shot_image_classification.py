# -*- coding: utf-8 -*-
"""zero-shot-image-classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hFskWyMEF3BnDIBSGcFtJ4R66xk-bex5
"""

# Hugging Face 라이브러리 설치
!pip install transformers
!pip install torch torchvision
!pip install pillow

# Hugging Face 관련 라이브러리 로드
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import os

# Hugging Face CLIP 모델 로드
model_id = "openai/clip-vit-base-patch32"  # CLIP 모델 ID
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)

# Colab에 이미지 업로드
from google.colab import files
uploaded = files.upload()

# 업로드된 파일 이름 확인 및 로드
image_path = list(uploaded.keys())[0]  # 업로드된 첫 번째 파일 사용
image = Image.open(image_path).convert("RGB")

# 분류 라벨 정의
labels = [
    "an apple",
    "an orange",
    "a flower",
    "a leaf",
    "a broccoli"
]

# 텍스트와 이미지를 처리하여 Zero-shot 예측
inputs = processor(
    text=labels,
    images=image,
    return_tensors="pt",
    padding=True
)
outputs = model(**inputs)

# logits 값에서 가장 높은 확률의 라벨 선택
logits_per_image = outputs.logits_per_image  # (batch_size, num_labels)
probs = logits_per_image.softmax(dim=1)  # 소프트맥스를 통해 확률 계산
predicted_class = labels[probs.argmax().item()]  # 가장 높은 확률의 라벨
probabilities = probs.squeeze().tolist()  # 확률 값 추출

# 결과 출력
print("Predicted class:", predicted_class)
for label, prob in zip(labels, probabilities):
    print(f"{label}: {prob:.4f}")
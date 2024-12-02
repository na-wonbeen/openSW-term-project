# Image Insight

## 프로젝트 개요

**Image Insight**는 이미지를 입력받아 이미지 속 사물을 탐지(OpenCV)하고, 이를 기반으로 Huggingface의 Vision-Language 모델(VIT-GPT2)을 사용해 사물에 대한 설명을 생성하는 오픈소스 프로그램입니다.

## 기능
1. OpenCV를 사용한 객체 탐지.
2. Huggingface Transformers 기반 텍스트 설명 생성.
3. 분석 결과를 출력하여 이미지의 의미를 자동으로 해석.

## 사용한 패키지 및 버전
- **Huggingface Transformers**: 4.33.3  
- **OpenCV**: 4.8.0

## 설치 명령
`requirements.txt` 파일을 사용해 필요한 패키지를 설치할 수 있습니다.
```bash
pip install -r requirements.txt

## 패키지 설치
pip install -r requirements.txt

## 이미지 분석
입력 이미지 경로를 지정하여 분석을 실행합니다.
python main.py --image images/input_example.jpg
결과는 터미널에 출력됩니다.

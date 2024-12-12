import cv2
import argparse


def main(image_path):
    # 1. 이미지 로드
    image = cv2.imread(r"C:\Users\USER\Desktop\424.jpg")
    if image is None:
        print("이미지를 불러올 수 없습니다.")
        return

    # 2. 객체 탐지
    objects = detect_objects(image)

    # 3. 설명 생성
    description = generate_description(objects)

    # 4. 결과 출력
    print("Generated Description:")
    print(description)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True, help="분석할 이미지 경로")
    args = parser.parse_args()

    main(args.image)






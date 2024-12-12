from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

# Huggingface 모델 로드
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_description(objects):
    descriptions = []

    for obj in objects:
        # OpenCV 이미지 -> PIL 이미지
        pil_image = Image.fromarray(cv2.cvtColor(obj, cv2.COLOR_BGR2RGB))
        pixel_values = feature_extractor(pil_image, return_tensors="pt").pixel_values

        # 설명 생성
        output_ids = model.generate(pixel_values)
        description = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        descriptions.append(description)

    return " ".join(descriptions)

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load the processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image
img_path = r"C:\Users\Partha\Desktop\sample_folder\sample.jpg"  # replace with your image path
image = Image.open(img_path).convert('RGB')

# Preprocess and generate caption
inputs = processor(images=image, return_tensors="pt")
out = model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

print("🖼️ Generated Caption:", caption)


import os
from PIL import Image

def load_images(image_directory):
    for filename in os.listdir(image_directory):
        if filename.endswith('.jpg'):  
            image_path = os.path.join(image_directory, filename)
            image = Image.open(image_path)
            yield image

image_directory ="C:/Users/PaulE/Documents/DataSet/AbstractArt"
images = [Image.open(os.path.join(image_directory,filename)) for filename in os.listdir(image_directory) if filename.endswith('.jpg')]
for i, img in enumerate(images):
    img.save(f"C:/Users/PaulE/Documents/DataSet/AbstractArt/test/processed_image_{i}.png")
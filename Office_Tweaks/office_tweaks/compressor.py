from PIL import Image


def compression(image_path: str, quality: int):
    image_file = Image.open(image_path)
    image_file.save(image_path, quality=quality)

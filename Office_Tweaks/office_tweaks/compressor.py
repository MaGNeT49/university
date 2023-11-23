from PIL import Image


def compression(image_path: str, quality: int):
    """
    Сжатие изображения
    :param image_path: путь или название файла в директории
    :param quality: Качество сжатия
    """
    image_file = Image.open(image_path)
    image_file.save(image_path, quality=quality)

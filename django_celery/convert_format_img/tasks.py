from celery import shared_task
from PIL import Image, ImageChops, ImageOps

@shared_task
def invert_image_colors(image_path):
    # Open the image using Pillow
    with Image.open(image_path) as im:
        # Invert the colors
        im = ImageOps.invert(im)
        # Save the inverted image
        im.save(image_path)

@shared_task        
def convert_image_to_black(image_path):
    # Open the image using Pillow
    with Image.open(image_path) as im:
        # Convert the image to grayscale
        im = ImageOps.grayscale(im)
        # Invert the colors
        im = ImageOps.invert(im)
        # Save the inverted image
        im.save(image_path)
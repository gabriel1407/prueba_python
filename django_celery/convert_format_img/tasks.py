from celery import shared_task
from PIL import Image, ImageChops

@shared_task
def invert_image_colors(image_path):
# Opening the test image, and saving it's object
    img = Image.open('./public/img/imagen_prueba.jpg')
    
    # Passing the image object to invert() 
    inv_img = ImageChops.invert(img)
    
    # Displaying the output image
    inv_img.show()
    
    inv_img.save(image_path)
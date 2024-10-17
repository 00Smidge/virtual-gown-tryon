# Set this up to automate image resizing
def resize(image, by_factor):
    new_img_size = (image.size[0] // by_factor, image.size[1] // by_factor)
    img_resize = image.resize(new_img_size)
    return img_resize

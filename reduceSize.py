import PIL
import os
from PIL import Image

trainImages = r'/mnt/c/Users/GANproject/1_Datasets/sculptures6k/sculptures6k_full/train'
saveImagesPath = "/mnt/c/Users/GANproject/1_Datasets/sculptures6k/sculptures6k_red"
counter = 2913
os.listdir()

pHeight = 480
pWidth = 480

for file in os.listdir(trainImages):
    f_img = trainImages +"/"+ file
    img = Image.open(f_img)
    width, height = img.size   # Get dimensions
    left = (width - pWidth)/2
    top = (height - pHeight)/2
    right = (width + pWidth)/2
    bottom = (height + pHeight)/2

    # Crop the center of the image
    img = img.crop((left, top, right, bottom))

    img.save(f"{saveImagesPath}/"+str(counter)+".png")
    counter += 1


# We could crop images from the center instead of a simple resize which might change the figure shape
# import Image
# im = Image.open(<your image>)
# width, height = im.size   # Get dimensions

# left = (width - new_width)/2
# top = (height - new_height)/2
# right = (width + new_width)/2
# bottom = (height + new_height)/2

# # Crop the center of the image
# im = im.crop((left, top, right, bottom))

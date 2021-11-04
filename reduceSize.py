import PIL
import os
from PIL import Image

trainImages = r'/mnt/d/GANtraining/1_Datasets/sculptures6k/train'
saveImagesPath = "/mnt/d/GANtraining/1_Datasets/sculptures6k/trainReduced"
counter = 0
os.listdir()

for file in os.listdir(trainImages):
    f_img = trainImages +"/"+ file
    img = Image.open(f_img)
    img = img.resize((320,320))
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
import os
from PIL import Image
cwd = os.getcwd()
# def  convert(width,height):
#     img_name = cwd+'/2 in1 mixer.png'

#     im = Image.open(img_name)
#     out = im.resize((width, height),Image.ANTIALIAS)
#     new_name = img_name.split('.')[0]+'_new'+'.png'
#     out.save(new_name) 
#     print('ok')

# convert(610,610)

from PIL import Image, ImageChops, ImageOps

def makeThumb(f_in, f_out, size=(610,610), pad=False):
    image = Image.open(f_in)
    image.thumbnail(size, Image.ANTIALIAS)
    image_size = image.size

    if pad:
        thumb = image.crop( (0, 0, size[0], size[1]) )

        offset_x = int(max( (size[0] - image_size[0]) / 2, 0 ))
        offset_y = int(max( (size[1] - image_size[1]) / 2, 0 ))

        thumb = ImageChops.offset(thumb, offset_x, offset_y)
        print('ok')

    else:
        thumb = ImageOps.fit(image, size, Image.ANTIALIAS, (0.5, 0.5))

    thumb.save(f_out)



for file in os.listdir(cwd):
    print(file)
    
    if (file.endswith('.png')):
        source = file
        paddeed = source.split('.')[0]+'_new_pad'+'.png'
        centerCrop = source.split('.')[0]+'_new_centerCropped.JPG'+'.png'
        makeThumb(source, paddeed, pad=True)
        print('ok')

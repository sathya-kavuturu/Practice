from PIL import Image, ImageFilter

img = Image.open('inception.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')
filtered_img.show()

grey_img = img.convert('L')
grey_img.save('grey.png', 'png')
grey_img.show()

rotated_img = filtered_img.rotate(180)
rotated_img.save("rotate.png", 'png')
rotated_img.show()

resize = img.resize((500,500))
resize.save('resize.png','png')
resize.show()

box = (100,100,400,400)
region = grey_img.crop(box)
region.save('crop.png','png')
region.show()

flower = Image.open('flower.jpg')
flower.thumbnail((400,200))
flower.save('thumbnail.png','png')
flower.show()

print(img)
img.show()
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))
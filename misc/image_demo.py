from PIL import Image, ImageEnhance, ImageFilter

img = Image.open('ladybug.jpg')
# img.show()
# new_img = img.convert('L')
# new_img.show()
# img.convert('1').show()
# img.convert('P').show()


rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0
)

img.convert("RGB", rgb2xyz).show()


# enhancer = ImageEnhance.Sharpness(img)
# for i in range(4):
#     factor = i / 2
#     enhancer.enhance(factor).show("Sharpness %f" % factor)

# enhancer = ImageEnhance.Color(img)
# for i in range(8):
#     factor = i / 4.0
#     enhancer.enhance(factor).show("Color %f" % factor)


# im1 = img.filter(ImageFilter.BLUR)
# im2 = img.filter(ImageFilter.MinFilter(3))
# im3 = img.filter(ImageFilter.MinFilter())  # same as MinFilter(3)

# im1.show()
# im2.show()
# im3.show()


# img.filter(ImageFilter.CONTOUR).show()
# img.filter(ImageFilter.EMBOSS).show()
# img.filter(ImageFilter.EDGE_ENHANCE).show()

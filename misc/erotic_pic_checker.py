from PIL import Image

file_name_1 = 'natarlie.jpg'
file_name_2 = 'test.jpg'

file_name = file_name_2

img = Image.open(file_name).convert('YCbCr')
w, h = img.size
data = img.getdata()
cnt = 0
for i, ycbcr in enumerate(data):
    y, cb, cr = ycbcr
    if 86 <= cb <= 117 and 140 <= cr <= 168:
        cnt += 1
print('%s %s a porn image.' %
      (file_name, 'is' if cnt > w * h * 0.3 else 'is not'))

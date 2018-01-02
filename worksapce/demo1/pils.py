#coding=utf-8;
from PIL import Image,ImageFilter;
img = Image.open('download/one.jpg');
imgfilter = img.filter(ImageFilter.GaussianBlur)
imgfilter.save("two.jpg")
imgfilter.show()

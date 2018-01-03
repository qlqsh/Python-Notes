#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

# 用Pillow对图片进行预处理。
kitten = Image.open("./Resources/kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("./Resources/kitten_bluerred.jpg")
blurryKitten.show()
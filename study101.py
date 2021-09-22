# PIL和pytesseract库使用。
# 没起作用

import pytesseract
from PIL import Image

image = Image.open("./pic/c.png")
code = pytesseract.image_to_string(image,lang="chi_sim")
print(code)
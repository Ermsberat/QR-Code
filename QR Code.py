# pip istall ile qrcode ve Image kütüphanesini indirmeyi unutmayınız.
# Do not forget to download the qrcode and Image library with pip install.
import qrcode
import os

os.system("clear")

print("""

this QR CODE was created by Berat

github.com/Ermsberat

""")

print("""
Lütfen Veriyi Giriniz

Please Enter Data
""")

data = input("Veri / Data: ")

image = qrcode.make(data)


image.save('qrkod.png')
image.show('qrkod.png')


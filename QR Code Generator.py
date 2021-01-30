import qrcode
from PIL import Image

input_URL = "https://www.google.com/"

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=15,border=4)
#error: This parameter sets the error correction level of the code.
#version: This parameter specifies the size and data capacity of the code.
#mode: This parameter sets how the contents will be encoded.
qr.add_data(input_URL)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("QRImage.png")
print(qr.data_list)
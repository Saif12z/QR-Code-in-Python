import qrcode
from PIL import Image  #importing image named file from pip
import qrcode.constants 

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4,) #QRcode changes functionality
qr.add_data("https://www.apnacollege.in/course/cpp-dsa")
qr.make(fit=True)
img = qr.make_image(fill_color ="White",back_color = "Black")
img.save("Apna college _ web.png")
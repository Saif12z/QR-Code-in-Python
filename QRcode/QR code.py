import qrcode as qr #importing qr code and making an alias
img = qr.make("https://www.youtube.com/@ApnaCollegeOfficial")
img.save("ApnaCollege_youtube.png")
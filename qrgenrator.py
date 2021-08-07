import qrcode
import image
qr = qrcode.QRCode(
    version= 7.2,
    box_size=10,
    border=5
)

data="https://github.com/login" #this data will use to add in qrcode


qr.add_data(data) #function add_data() is used to add data in qrcode

qr.make(fit = True)

img = qr.make_image(fill_color="black",back_color="white")

img.save("test.png")
from textwrap import fill
import qrcode
import image
qr =qrcode.QRCode(
    version=15, 
    box_size=10,
    border=5,
)
data = input("Enter the Link :-")

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
nme = input("Enter your Qrcode naame you want")
img = (img.save(nme)) #please enter your name with png

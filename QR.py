import qrcode

myqr= qrcode.make("n")  # Remove 'n' and enter the URL, text, or message you wish to convert into a QR code. 

myqr.save("myqr.png")

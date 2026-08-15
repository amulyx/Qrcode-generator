import qrcode 
data = input("Enter the text or link: ")
img = qrcode.make(data)
img.save("qr.png")
img.show()
print(" Qrcode successfully completed!! ")
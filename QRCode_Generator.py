import qrcode 

# Qr Code Generator

# Input the url 
url=input("Enter the URL to be generated: ").strip()

# File path: C:\\Users\\shobh\\OneDrive\\Desktop\\ otherwise in this folder only
file_location="qrcode.png"

qr=qrcode.QRCode() #Qr code maker
qr.add_data(url) # Adding data to QR

image=qr.make_image()   # Generating Image
image.save(file_location) # Saving image to this folder as qrcode.png

print("QR Code Generated Successfully!")



import qrcode

# For money Transfer

# Taking upi id as input

upi_id=input("Enter the upi id: ").strip()

file_path="qrcode.png"

#upi://pay?pa=UPI_ID&pn=Recipent_Name&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepe_url=f"upi://pay?pa={upi_id}&pn=Recipent"

# Create QR code for payment app

phonepe_qr=qrcode.QRCode()
phonepe_qr.add_data(phonepe_url)

image=phonepe_qr.make_image()

image.save(file_path)
print("QR Code Generated Successfully!")
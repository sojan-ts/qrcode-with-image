import qrcode

# taking URL or text for the QR code
url = "https://sojansir.com"

# creating QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# adding data (URL or text) to the QR code
qr.add_data(url)
qr.make(fit=True)

# generating QR code image
qr_img = qr.make_image(fill_color="#000000", back_color="white")

# save the QR code image
qr_img.save("simple_QR.png")

print("Simple QR code generated!")

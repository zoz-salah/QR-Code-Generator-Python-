import qrcode

url = "https://www.https://github.com/zoz-salah"
file = "D:\\save\\GITHUB_qr_code.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file)

print("QR code generated and saved successfully.")

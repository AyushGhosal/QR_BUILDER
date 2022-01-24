import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)
qr.add_data("https://ayushghosal2021.wixsite.com/website")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("Qr_code.png")

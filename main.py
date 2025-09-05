import qrcode

website_link = input("Please give me your website: ")

qr = qrcode.QRCode(version = 5, box_size = 5, border = 5)

qr.add_data(website_link)

qr.make()

img = qr.make_image(fill_color = 'black', back_color = "white")

img.save("output_qr.png")
img.show()


import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level: L, M, Q, or H
    box_size=10,  # Size of each box in pixels
    border=4  # Border size in boxes
)

# Data to be encoded in the QR code
data = "Hello, World!"

# Add data to the QR code
qr.add_data(data)

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image as a file
qr_image.save("qrcode.png")

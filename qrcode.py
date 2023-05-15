# creating a QR code
# import PyQRCode, pypng

import pyqrcode
import png

link = "https://docs.google.com/document/d/15xTc_Cz7pih9crstmuh694dMKYraYSUc/edit?usp=sharing&ouid=113759765345959356518&rtpof=true&sd=true"
qr_code = pyqrcode.create(link)
qr_code.png("resume.png", scale=5)

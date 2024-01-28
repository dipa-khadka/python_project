# Importing the library form the package
import qrcode

# Generate the QR code
img = qrcode.make('https://www.youtube.com/channel/UCJZKDZd2w5dLFvssNdP_jvg')

# Saving the image as image file like(.jpg)
img.save('YouTubeQRCode.jpg')

img.show('YouTubeQRCode.jpg')
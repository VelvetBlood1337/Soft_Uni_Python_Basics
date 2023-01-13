import pyqrcode

address = 'example.com'
url = pyqrcode.create(address)
url.png('example.png', scale=8)

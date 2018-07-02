import pyqrcode

qr = pyqrcode.create('https://github.com/mary333')
qr.png('qr.png', scale=6, module_color="#FA8072")
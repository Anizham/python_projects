import pyqrcode
import png
from pyqrcode import QRCode
QRstring="url"
url=pyqrcode.create(QRstring)
url.png('qrcode.png',scale=8)

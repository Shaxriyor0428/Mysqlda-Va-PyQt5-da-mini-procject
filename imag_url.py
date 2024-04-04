from PyQt5.QtWidgets import QApplication ,QWidget,QLabel
from PyQt5.QtGui import QPixmap,QIcon,QImage
import requests

app = QApplication([])
url = "https://olcha.uz/image/400x400/products/2022-10-14/tkan-kunlar-abdulla-odiriy-156236-0.jpeg"
image = QImage()
image.loadFromData(requests.get(url).content)
lbl = QLabel()
lbl.setPixmap(QPixmap(image))

lbl.show()
app.exec()



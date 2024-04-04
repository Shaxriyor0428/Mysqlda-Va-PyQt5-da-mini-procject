from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from bookCategoryRepsitory import BookInterface
import requests


class BookDetailWindow(QWidget):
    def __init__(self, bookDetail: BookInterface):
        super().__init__()
        self.bookDetail = bookDetail
        self.setFixedSize(500, 500)

        self.showInfoOfBook()

    def showInfoOfBook(self):
        self.vLyaout = QVBoxLayout(self)

        label_author = QLabel("Author: " + self.bookDetail.author)
        label_name = QLabel("Book Name: " + self.bookDetail.name)
        label_year = QLabel("Book Year: " + str(self.bookDetail.year))
        label_image = QLabel()


        image_url = self.bookDetail.imageUrl
        response = requests.get(image_url)
        
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            label_image.setPixmap(pixmap.scaledToWidth(200))

        self.vLyaout.addWidget(label_author)
        self.vLyaout.addWidget(label_name)
        self.vLyaout.addWidget(label_year)
        self.vLyaout.addWidget(label_image)

        self.setLayout(self.vLyaout)

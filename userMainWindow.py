from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QCheckBox,QHBoxLayout,QVBoxLayout,QListWidget,QMessageBox,QListWidgetItem
from index import Repsitory
from bookCategoryRepsitory import BookInterface
from BookDatialWindow import BookDetailWindow

class UserMainwindow(QWidget):
    def __init__(self,userId):
        super().__init__()
        self.setFixedSize(500,500)
    
        self.listwidget = QListWidget(self)
        self.listwidget.setGeometry(30,30,350,350)
        books = Repsitory().Bookrepsitoryall().getList(userID=userId,size=100)

        if not books:
            self.Messgage("Ushbu userda kitoblar yo'q")
            self.close()
        else:
            showdata = []
            for item in books:
                newItem = QListWidgetItem(item.name)
                newItem.data = item
                showdata.append(newItem)

        self.setItemtoList(showdata)

        self.listwidget.itemClicked.connect(self.BookDatial)
        
    def setItemtoList(self,lst:list[BookInterface]):
        self.listwidget.clear()
        for item in lst:
            self.listwidget.addItem(item)



    def Messgage(self,message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()


    def BookDatial(self) :
        item: BookInterface = self.listwidget.currentItem().data
        self.bookDatialWin = BookDetailWindow(item)
        self.bookDatialWin.show()


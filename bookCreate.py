from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QCheckBox,QHBoxLayout,QVBoxLayout,QMessageBox,QCompleter
from index import Repsitory

class GetInfo():
    def __init__(self):
        self.info = Repsitory().userRepsitory().getByName()
        self.janr = Repsitory().categoryRepsitory().getByName()

    def GetNameInfo(self):
        names = []
        for item in self.info:
            names.append(item[3])
        result = [i.lower() for i in names]
        return result

    def getCategoryName(self):
        names = []
        for item in self.janr:
            names.append(item[1])
        result = [i.lower() for i in names]
        return result


class BookCreate(QWidget):
  
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,400)
 
        self.nameBook = QLineEdit(self)
        self.namelbl = QLabel("Name",self)
        self.nameBook.setStyleSheet("font-size:15px")
        self.namelbl.setStyleSheet("font-size:15px")
        self.nameBook.setPlaceholderText("Kitob nomi..")

        self.g = QHBoxLayout()
        self.g.addWidget(self.namelbl)
        self.g.addWidget(self.nameBook)

        self.bookAftor = QLineEdit(self)
        self.boklbl = QLabel("Kitob muallifi ",self)
        self.bookAftor.setPlaceholderText("Muallif..")
        self.bookAftor.setStyleSheet("font-size:15px")
        self.boklbl.setStyleSheet("font-size:15px")
        
        self.g1 = QHBoxLayout()
        self.g1.addWidget(self.boklbl)
        self.g1.addWidget(self.bookAftor)

        self.bookyear = QLineEdit(self)
        self.booklbl = QLabel("Kitob yili",self)
        self.g2 = QHBoxLayout()
        self.g2.addWidget(self.booklbl)
        self.g2.addWidget(self.bookyear)
        self.bookyear.setStyleSheet("font-size:15px;")
        self.booklbl.setStyleSheet("font-size:15px;")
        self.bookyear.setPlaceholderText("Kitob yili..")

        self.bookUrl = QLineEdit(self)
        self.booklbl = QLabel("Kitob Url",self)
        self.g3 = QHBoxLayout()
        self.g3.addWidget(self.booklbl)
        self.g3.addWidget(self.bookUrl)
        self.bookUrl.setStyleSheet("font-size:15px;")
        self.booklbl.setStyleSheet("font-size:15px;")
        self.bookUrl.setPlaceholderText("Kitob urli..")

        obj = GetInfo()
        self.categoryName = QCompleter(obj.getCategoryName())
        self.names = QCompleter(obj.GetNameInfo())
        self.bookOwner = QLineEdit(self)
        self.bookOwner.setCompleter(self.names)
        self.booklbl = QLabel("Kitob egasi",self)
        self.g4 = QHBoxLayout()
        self.g4.addWidget(self.booklbl)
        self.g4.addWidget(self.bookOwner)  
        self.booklbl.setStyleSheet("font-size:15px;")
        self.bookOwner.setStyleSheet("font-size:15px;")
        self.bookOwner.setPlaceholderText("kitob egasinig ismi..")

        self.btnSubmit = QPushButton("Submit",self)
        self.btnSubmit.setStyleSheet("font-size:20px;")

        self.btnSubmit.setGeometry(180,360,150,35)
        self.kitobCategory = QLineEdit(self)
        self.Kitobcatelbl = QLabel("Kitob janri")
        self.kitobCategory.setCompleter(self.categoryName)
        self.g5 = QHBoxLayout()
        self.g5.addWidget(self.Kitobcatelbl)
        self.g5.addWidget(self.kitobCategory)
        self.kitobCategory.setStyleSheet("font-size:15px;")
        self.Kitobcatelbl.setStyleSheet("font-size:15px;")
        self.kitobCategory.setPlaceholderText("kitob egasinig ismi..")

        self.v = QVBoxLayout()
        self.v.addLayout(self.g)
        self.v.addLayout(self.g1)
        self.v.addLayout(self.g2)
        self.v.addLayout(self.g3)
        self.v.addLayout(self.g4)
        self.v.addLayout(self.g5)
        self.setLayout(self.v)
        self.btnSubmit.setEnabled(False)
        self.nameBook.textChanged.connect(self.Textchanged)
        self.bookAftor.textChanged.connect(self.Textchanged)
        self.bookyear.textChanged.connect(self.Textchanged)
        self.bookUrl.textChanged.connect(self.Textchanged)
        self.bookOwner.textChanged.connect(self.Textchanged)
        self.kitobCategory.textChanged.connect(self.Textchanged)

        self.btnSubmit.clicked.connect(self.bookCreate)

        
    def bookCreate(self):
        data1 = Repsitory().userRepsitory().getByUserName(username=self.bookOwner.text())
        data2 = Repsitory().categoryRepsitory().getByUserName(name=self.kitobCategory.text())
        if data1:
            obj = Repsitory().Bookrepsitoryall().create(
                name=self.nameBook.text(),
                author=self.bookAftor.text(),
                year=self.bookyear.text(),
                imageUrl=self.bookUrl.text(),
                userID=data1.id,
                categoryID=data2.id
            )
            self.messageBox("Muvvafaqiyatli yaratildi!")
            self.nameBook.clear()
            self.bookAftor.clear()
            self.bookyear.clear()
            self.bookUrl.clear()
            self.bookOwner.clear()
            self.kitobCategory.clear()
        else:
            self.messageBox("Kitob yaratishda xatolik")
        

    def messageBox(self,item):
        msg = QMessageBox()
        msg.setText(item)
        msg.exec()

    def Textchanged(self):
        if len(self.nameBook.text()) > 0 and len(self.bookAftor.text()) > 0 and len(self.bookyear.text()) > 0 and len(self.bookUrl.text()) > 0 and len(self.bookOwner.text()) > 0 and len(self.kitobCategory.text()) > 0:
            self.btnSubmit.setEnabled(True)
        else:
            self.btnSubmit.setEnabled(False)

# app = QApplication([])
# win = BookCreate()
# win.show()
# app.exec()

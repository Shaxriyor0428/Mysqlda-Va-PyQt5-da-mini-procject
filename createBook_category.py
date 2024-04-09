from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QCheckBox,QMessageBox,QCompleter,QHBoxLayout,QVBoxLayout
from index import Repsitory

class CreateBookCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Book Category")
        self.setFixedSize(400,300)
            
        self.liniCategoryName = QLineEdit(self)
        self.lblCategoryName = QLabel("Kitob category",self)
        self.liniCategoryName.setStyleSheet("font-size:15px")
        self.lblCategoryName.setStyleSheet("font-size:15px")
        self.liniCategoryName.setPlaceholderText("Kitob janrini kiriting..")

        self.g = QHBoxLayout()
        self.g.addWidget(self.lblCategoryName)
        self.g.addWidget(self.liniCategoryName)

        self.btnSubmit = QPushButton("Save",self)
        self.v = QVBoxLayout() 

        self.g1 = QHBoxLayout(self.btnSubmit)

        self.v.addLayout(self.g)
        self.v.addWidget(self.btnSubmit)
        self.setLayout(self.v)
        self.btnSubmit.clicked.connect(self.CategorySave)

    def CategorySave(self):
        if len(self.liniCategoryName.text()) > 0 :
            categoryObj = Repsitory().categoryRepsitory().create(name=self.liniCategoryName.text())
            self.MessageBox("Muvvafaqiyatli yaratildi!")
            self.liniCategoryName.clear()
        else:
            self.MessageBox("Yaratishda xatolik!")


    def MessageBox(self,message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()

# app = QApplication([])
# window = CreateBookCategory()
# window.show()
# app.exec()
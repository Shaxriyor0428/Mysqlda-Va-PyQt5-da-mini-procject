

from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QCheckBox,QHBoxLayout,QVBoxLayout,QMessageBox
from index import Repsitory

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,400)
    
        self.liniAge = QLineEdit(self)
        self.lblAge = QLabel("age",self)
        self.liniAge.setStyleSheet("font-size:15px")
        self.lblAge.setStyleSheet("font-size:15px")
        self.liniAge.setPlaceholderText("Yoshingiz..")

        self.g = QHBoxLayout()
        self.g.addWidget(self.lblAge)
        self.g.addWidget(self.liniAge)

        self.liniUser = QLineEdit(self)
        self.lbluser = QLabel("Username",self)
        self.liniUser.setPlaceholderText("Username..")
        self.liniUser.setStyleSheet("font-size:15px")
        self.lbluser.setStyleSheet("font-size:15px")
        
        self.g1 = QHBoxLayout()
        self.g1.addWidget(self.lbluser)
        self.g1.addWidget(self.liniUser)

        self.Eemail = QLineEdit(self)
        self.lemail = QLabel("Email",self)
        self.g2 = QHBoxLayout()
        self.g2.addWidget(self.lemail)
        self.g2.addWidget(self.Eemail)
        self.Eemail.setStyleSheet("font-size:15px;")
        self.lemail.setStyleSheet("font-size:15px;")
        self.Eemail.setPlaceholderText("@email..")

        self.passwordEdit = QLineEdit(self)
        self.passwordLbl = QLabel("Password",self)
        self.g3 = QHBoxLayout()
        self.g3.addWidget(self.passwordLbl)
        self.g3.addWidget(self.passwordEdit)
        self.passwordEdit.setStyleSheet("font-size:15px;")
        self.passwordLbl.setStyleSheet("font-size:15px;")
        self.passwordEdit.setPlaceholderText("Password..")


        self.repetPasEdit = QLineEdit(self)
        self.repetPasLbl = QLabel("Repit password",self)
        self.g4 = QHBoxLayout()
        self.g4.addWidget(self.repetPasLbl)
        self.g4.addWidget(self.repetPasEdit)  
        self.repetPasLbl.setStyleSheet("font-size:15px;")
        self.repetPasEdit.setStyleSheet("font-size:15px;")
        self.repetPasEdit.setPlaceholderText("Repit pass.")

        self.btnSubmit = QPushButton("Submit",self)
        self.btnSubmit.setStyleSheet("font-size:20px;")

        self.btnSubmit.setGeometry(180,360,150,35)
        

        self.v = QVBoxLayout()
        self.v.addLayout(self.g)
        self.v.addLayout(self.g1)
        self.v.addLayout(self.g2)
        self.v.addLayout(self.g3)
        self.v.addLayout(self.g4)
        self.setLayout(self.v)

        self.liniAge.textChanged.connect(self.Textchanged)
        self.liniUser.textChanged.connect(self.Textchanged)
        self.Eemail.textChanged.connect(self.Textchanged)
        self.passwordEdit.textChanged.connect(self.Textchanged)
        self.repetPasEdit.textChanged.connect(self.Textchanged)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.repetPasEdit.setEchoMode(QLineEdit.Password)

        self.chBox = QCheckBox(self)
        self.chBox.move(360,230)
        self.chBox.clicked.connect(self.showPassword)
        self.btnSubmit.clicked.connect(self.AllConnetionCreate)
    def showPassword(self):
        if self.chBox.isChecked():
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)

        if self.chBox.isChecked():
            self.repetPasEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.repetPasEdit.setEchoMode(QLineEdit.Password)

        
    def AllConnetionCreate(self):
        try:
            if self.passwordEdit.text() == self.repetPasEdit.text():
                repoOj = Repsitory()
                repoOj.userRepsitory().create(self.passwordEdit.text(),self.liniAge.text(),self.liniUser.text(),self.Eemail.text())
                self.messageBox(str("Muvvaqiyatli yozildi"))
                self.liniAge.clear()
                self.liniUser.clear()
                self.passwordEdit.clear()
                self.Eemail.clear()
                self.repetPasEdit.clear()
            else:
                raise Exception("Xato Repit password")
            
        except Exception as error:
            self.messageBox(str(error))

    def messageBox(self,item):
        msg = QMessageBox()
        msg.setText(item)
        msg.exec()

    def Textchanged(self):
        if len(self.liniAge.text()) > 0 and len(self.liniUser.text()) > 0 and len(self.Eemail.text()) > 0 and len(self.passwordEdit.text()) > 0 and len(self.repetPasEdit.text()) > 0:
            self.btnSubmit.setEnabled(True)
        else:
            self.btnSubmit.setEnabled(False)



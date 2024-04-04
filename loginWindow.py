from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QCheckBox,QMessageBox
from index import Repsitory
from userMainWindow import UserMainwindow


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,300)
    
        self.liniUser = QLineEdit(self)
        self.liniUser.move(150,20)
        self.liniUser.textChanged.connect(self.LoginOnoff)
        self.liniPass = QLineEdit(self)
        self.liniPass.move(150,50)
        self.liniPass.textChanged.connect(self.LoginOnoff)

        self.lblUser = QLabel("Username",self)
        self.lblUser.move(50,25)
        self.lblPass = QLabel("Password",self)
        self.lblPass.move(50,55)
        self.btnLogin = QPushButton("Login",self)
        self.btnRegister = QPushButton("Register",self)




        self.btnRegister.move(150,200)
        self.btnLogin.move(150,150)
        self.liniUser.setStyleSheet("font-size:20px;")
        self.liniPass.setStyleSheet("font-size:20px;")
        self.btnLogin.setStyleSheet("font-size:20px;")
        self.btnRegister.setStyleSheet("font-size:20px;")
        self.lblPass.setStyleSheet("font-size:20px;")
        self.lblUser.setStyleSheet("font-size:20px;")
        self.liniPass.setPlaceholderText("Password..")
        self.liniUser.setPlaceholderText("Username..")

        self.chBox = QCheckBox(self)
        self.chBox.move(360,60)
        self.chBox.clicked.connect(self.showPassword)
        self.btnLogin.clicked.connect(self.checkInfo)
        self.liniPass.setEchoMode(QLineEdit.Password)
        self.btnRegister.clicked.connect(self.registratsiya)
        self.btnBack = QPushButton("Back",self)
        self.btnBack.setStyleSheet("font-size:20px;color:red")
        self.btnBack.move(150,250)
        self.btnBack.clicked.connect(self.backClose)
    def showPassword(self):
        if self.chBox.isChecked():
            self.liniPass.setEchoMode(QLineEdit.Normal)
        else:
            self.liniPass.setEchoMode(QLineEdit.Password)

    def LoginOnoff(self):
        if len(self.liniUser.text()) > 0 and len(self.liniPass.text()) > 0:
            self.btnLogin.setEnabled(True)
        
        else:
            self.btnLogin.setEnabled(False)



    def checkInfo(self):
        try:
            userRepoObj = Repsitory()
            user = userRepoObj.userRepsitory().getByUserName(self.liniUser.text())
            if user:
                if user.password == self.liniPass.text():
                    self.userMainWin = UserMainwindow(user.id)
                    self.userMainWin.show()
                    self.close()
                else:
                    raise Exception("Password xato")
            else:
                raise Exception("Username topilmadi")

        except Exception as error:
            self.messagBox(str(error))

            self.liniPass.clear()
            self.liniUser.clear()

    def registratsiya(self):
        from registrLogin import Register
        self.obj = Register()
        self.obj.show()
        self.close()


    def messagBox(self,message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()

    def backClose(self):
        self.close()

app = QApplication([])
window = Mainwindow()
window.show()
app.exec()

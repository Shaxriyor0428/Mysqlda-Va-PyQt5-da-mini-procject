import mysql.connector

class Connection:
    def __init__(self,host = "localhost",user = "root",password = "shaxriyor",database = "Home_work"):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

        self.__start()
    
    def __start(self):
        self.dataBaseConnection = mysql.connector.connect(
            user = self.__user,
            host = self.__host,
            password = self.__password,
            database = self.__database
        )

        self.dataBaseCursor = self.dataBaseConnection.cursor()


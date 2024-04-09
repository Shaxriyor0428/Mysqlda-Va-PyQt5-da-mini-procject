"""
id ,username,password ,age,email
CREATE TABLE users (id varchar(50) UNIQUE,password varchar(100),age INT,username varchar(50) UNIQUE,email varchar(100) UNIQUE,PRIMARY KEY);
"""
# ushbu class orqal malumotlarni shablonga olayabmiz
from uuid import uuid4

class UserInterface:
    id :str = None
    password :str = None
    age : int = None
    username:str = None
    email :str = None
    def __init__(self,data:tuple):
        self.id = data[0]
        self.password = data[1]
        self.age = data[2]
        self.username = data[3]
        self.email = data[4]
        

class UserRepsitory:
    def __init__(self,dbCon,dbCur):
        self.dbCur = dbCur
        self.dbCon = dbCon
        

    def  create(self,password,age,username,email):
        query = "INSERT INTO users(id,password,age,username,email) VALUES (%s,%s,%s,%s,%s)"
        self.dbCur.execute(query,(str(uuid4()),password,age,username,email))
        self.dbCon.commit()

        
    def getById(self,id):
        query = "SELECT * FROM users where id = %s"
        self.dbCur.execute(query,(id,))
        data = self.dbCur.fetchall()
        if len(data):
            return UserInterface(data[0])
        else:
            return None

        
    def getByUserName(self,username):
        query = "SELECT * FROM users where username = %s"
        self.dbCur.execute(query,(username,))
        data = self.dbCur.fetchall()

        if len(data):
            return UserInterface(data[0])
        else:
            return None

    def getByName(self):
        query = "SELECT * FROM users"
        self.dbCur.execute(query)
        data = self.dbCur.fetchall()

        return data
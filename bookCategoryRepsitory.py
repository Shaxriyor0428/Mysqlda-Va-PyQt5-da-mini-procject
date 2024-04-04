"""


CREATE TABLE Books (id varchar(100) PRIMARY KEY,name varchar(100) UNIQUE,
categoryID varchar(100),userID varchar(100),year int,
author varchar(100),imageUrl varchar(200),FOREIGN KEY(categoryID) REFERENCES category (id),
FOREIGN KEY (userID) REFERENCES users(id));

"""
from uuid import uuid4

class BookInterface:
    id :str = None
    name :str = None
    categoryID :str = None
    userID :str = None
    year :str = None
    author:str = None
    imageUrl:str = None

    def __init__(self,data:tuple) :
        self.id = data[0]
        self.name = data[1]
        self.categoryID = data[2]
        self.userID = data[3]
        self.year = data[4]
        self.author = data[5]
        self.imageUrl = data[6]


class BookRepsitory:
    def __init__(self, dbCon,dbCur) :
        self.dbCon = dbCon
        self.dbCur = dbCur

    
    def create (self,name,categoryID,userID,year,author,imageUrl):
        query = "INSERT INTO Books (id,name,categoryID,userID,year,author,imageUrl) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        self.dbCur.execute(query,(str(uuid4()),name,categoryID,userID,year,author,imageUrl))
        self.dbCon.commit()
        

    def getById(self,id) -> BookInterface:
        query = "SELECT * FROM Books WHERE id = %s"
        self.dbCur.execute(query,(id,))
        data = self.dbCur.fetchall()
        if len(data):
            return BookInterface(data[0])
        else:
            return None
     
    def getList(self, page = 1, size = 100, search = '',userID= 'cb6468bd-f076-4711-98bd-534c6a4b0157') -> list[BookInterface]:
        query = "SELECT * FROM Books where name like CONCAT('%',%s,'%') and userID = %s LIMIT %s OFFSET %s"
        self.dbCur.execute(query,(search ,userID, size, (size * (page -  1))))
    
        data = self.dbCur.fetchall()
        response = []

        for item in data:
            response.append(BookInterface(item))

        return response

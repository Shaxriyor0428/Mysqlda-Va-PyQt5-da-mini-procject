"""
CREATE TABLE category(id varchar(100),name varchar(100) UNIQUE PRIMARY KEY(id));
"""

from uuid import uuid4

class CategoryInterface:
    id :str = None
    name :str = None

    def __init__(self,data:tuple) :
        self.id = data[0]
        self.name = data[1]

class CategoryRepsitory:
    def __init__(self, dbCon,dbCur) :
        self.dbCon = dbCon
        self.dbCur = dbCur

    
    def create (self,name):
        query = "INSERT INTO category (id,name) VALUES(%s,%s)"
        self.dbCur.execute(query,(str(uuid4()),name))
        self.dbCon.commit()
        

    def getById(self,id) -> CategoryInterface:
        query = "SELECT * FROM category WHERE id = %s"
        self.dbCur.execute(query,(id,))
        data = self.dbCur.fetchall()

        if len(data):
            return CategoryInterface(data[0])
        else:
            return None
     
        

    def getList(self,page,size,search) -> list[CategoryInterface]:
        query = "SELECT * FROM category WHERE name like CONCAT('%', %s,'%') LIMIT %s OFFSET %s"

        self.dbCur.execute(query,(search,size, (size * (page - 1))))

        data = self.dbCur.fetchall()
        response = []

        for item in data:

            response.append(CategoryInterface(item))
        return response
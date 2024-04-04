from dbConnection import Connection
from UserRepsitory import UserRepsitory
from categoryRepsitory import CategoryRepsitory
from bookCategoryRepsitory import BookRepsitory


from uuid import uuid4
class Repsitory(Connection):
    def __init__(self):
        super().__init__()

        
    def userRepsitory(self):
        obj = UserRepsitory(self.dataBaseConnection,self.dataBaseCursor)
        return obj

    def categoryRepsitory(self):
        obj1 = CategoryRepsitory(self.dataBaseConnection,self.dataBaseCursor)
        return obj1
    
    def Bookrepsitoryall(self):
        obj2 = BookRepsitory(self.dataBaseConnection,self.dataBaseCursor)
        return obj2
    

obj = Repsitory()

# obj.userRepsitory().create("hello14",18,"Mahliyo","mamnun@gamil.com")
# data = obj.userRepsitory().getById("cb6468bd-f076-4711-98bd-534c6a4b0157").username
# print(data)
# obj.categoryRepsitory().create("Science")
# print(obj.categoryRepsitory().getList(1,5,"")[1].name)



# obj.Bookrepsitoryall().create(
#     name="Mehrobdan Chayon",
#     categoryID="ea3163cd-00b4-4b28-810b-c48e29c351a9",
#     userID="95ba2335-dfcb-4604-ac4d-dfca2f941e5c",
#     year=1969,
#     author="Abdulla Qodiriy",
#     imageUrl="https://olcha.uz/image/400x400/products/2022-10-14/tkan-kunlar-abdulla-odiriy-156236-0.jpeg"
# )

# a = obj.Bookrepsitoryall().getById("8e6a8979-1ebb-423c-9817-335e4e6a6cfe").year

# b = obj.Bookrepsitoryall().getList()[0].name
# print(b)

# print(obj.userRepsitory().getByUserName("shodmon"))


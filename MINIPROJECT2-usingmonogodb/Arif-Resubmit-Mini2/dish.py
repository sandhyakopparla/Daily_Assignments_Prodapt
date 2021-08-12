import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydatabase= client["Mini1Db"]
Collection_name =mydatabase["dish"]

dish1=10
dish2=20
dish3=30
dish4=40
dish5=50
dict2={"dish1":dish1,"dish2":dish2,"dish3":dish3,"dish4":dish4,"dish5":dish5}
result=Collection_name.insert_one(dict2)
print(result)
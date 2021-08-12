import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydata=client["Busdb"]
locationcollection=mydata["Location"]
places=[{"source":"Cuddalore","1":{"stop":"Pondicherry" ,"price":"100"},"2":{"stop":"Mahabalipuram" ,"price":"200"},"3":{"stop":"Chennai" ,"price":"300"}}]
#result=locationcollection.insert_many(places)
#print(result)
result1=locationcollection.find()
mydata="Cuddalore"
#choice=input("Enter the choice : ")
for i in result1:
    if mydata==i['source']:
        choice=input("Enter the choice : ")
        destination=i[choice]
        print(destination)
        dict1={"source":i["source"],"destination":destination['stop'],"price":destination['price']}
        print(dict1)
        break
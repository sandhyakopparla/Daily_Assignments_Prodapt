import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['CricketersssDb']
collection_name=mydatabase['cricketers']
def updatedetails():
    while(True):
        print("1.update the location")
        print("2.update the matchone score")
        print("3.update the matchtwoscore")
        print("4.update the team")
        print("5.exit")
        ch=int(input("enter your choice"))
        if ch==1:
            c=input("enter the cricketer_name")
            l=input("enter the location to be updated")
            result=collection_name.update_one({"cricketer_name":c},{"$set":{"location":l}})
            print(result)
        if ch==2:
            c=input("enter the cricketer_name")
            l=input("enter the matchone_score to be updated")
            result=collection_name.update_one({"cricketer_name":c},{"$set":{"matchone_score":l}})
            print(result)
        if ch==3:
            c=input("enter the cricketer_name")
            l=input("enter the matchtwo_score to be updated")
            result=collection_name.update_one({"cricketer_name":c},{"$set":{"matchtwo_score":l}})
            print(result)
        if ch==4:
            c=input("enter the cricketer_name")
            l=input("enter the team to be updated")
            result=collection_name.update_one({"cricketer_name":c},{"$set":{"team":l}})
            print(result)
        if ch==5:
            break

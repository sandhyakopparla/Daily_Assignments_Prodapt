import re,logging,pymongo
from valimodule import validation_of_cricketers
import updatemodule
cricketerlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['CricketersssDb']
collection_name=mydatabase['cricketers']
class Cricketers:
    def addcricketerdetails(self,cricketer_name,matchone_score,matchtwo_score,location,team,batting_style,bowling_style):
        dict1={"cricketer_name":cricketer_name,"matchone_score":matchone_score,"matchtwo_score":matchtwo_score,"location":location,"team":team,"batting_style":batting_style,"bowling_style":bowling_style}
        print(dict1)
        cricketerlist.append(dict1)
obj=Cricketers()
while(True):
    print("1.add the cricketers details:")
    print("2.view the details in db")
    print("3.search for the particular person in a batsmanlist")
    print("4.update the details")
    print("5.delete")
    print("6.count the players")
    print("7.Exit")
    choice=int(input("enter the choice"))
    if choice==1:
        cricketer_name=input("enter the batsman_name:")
        matchone_score=input("enter the matchone_score")
        matchtwo_score=input("enter the matchtwo_score")
        location=input("enter the b_location")
        team=input("enter the team")
        batting_style=input("enter the batting style")
        bowling_style=input("enter the bowling style")
        if validation_of_cricketers(cricketer_name,location,batting_style,bowling_style):
            obj.addcricketerdetails(cricketer_name,matchone_score,matchtwo_score,location,team,batting_style,bowling_style)
            result=collection_name.insert_many(cricketerlist)
            print(result.inserted_ids)
        else:
            logging.error("please enter valid details")
    if choice==2:
        result=collection_name.find()
        for i in result:
            cricketerlist.append(i)
            print(i)
    if choice==3:
        name=input("enter the name to search:")
        result=collection_name.find({"cricketer_name":name})
        for i in result:
            print(i)
    if choice==4:
        updatemodule.updatedetails()
    if choice==5:
        de=input("enter the bats_name") 
        result=collection_name.delete_many({"cricketer_name":de})
        print(result.deleted_count)
    if choice==6:
        result=collection_name.aggregate([{"$group":{"_id":"$team","no_of_cricketers":{"$sum":1}}}])
        for i in result:
            print(i) 
    if choice==7:
        break

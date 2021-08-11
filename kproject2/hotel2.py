import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing a connection
mydatabase=client['hotelmangeDb']        
collection_name=mydatabase['hotelmange']

import pytz
from datetime import datetime

standardtime=pytz.utc
timezone=pytz.timezone("Asia/kolkata")
print(datetime.now(standardtime))
print(datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S"))


hotellist=[]
hotelview=[]

class hotelmanage:

    def idata(self,name,address,phno,cindate,coutdate,rno):
        dic={"name":name,"phno":phno,"address":address,"cindate":cindate,"coutdate":coutdate,"rno":rno}
        hotellist.append(dic)

obj1=hotelmanage()

while(True):
    print ("WELCOME TO HOTEl\n")
    print("1. Enter Customer Data: ")
    print("2. view the customer details: ")
    print("3. search customer using name :")
    print("4. update the customer name :")
    print("5. delete the customer data using name: ")
    print("6. To view the customer name greater than e: ")
    print("7. to view the customer name less than b:")
    print("8. to count no  phone number:")
    print("9. EXIT")

    choice=int(input("\nEnter the number of your choice:"))
    if (choice==1):
        name=input("\nEnter your Fullname:")
        address=input("\nEnter your address:")
        phno=int(input("\nenter the phon no: "))
        cindate=input("\nEnter your check in date:")
        coutdate=input("\nEnter your checkout date:")
        rno=int(input("\nYour room no:"))
        
        # data={"name":name,"adress":adress,"cindate":cindate,"coutdate":coutdate,"roomno":rno}
        # print(data)

        def val(name,adress):
            val1=re.search("^[a-z]?[A-Z]",name)
            val2=re.search("^[A-Z]",adress)
            val3=re.search("^[1-9]\d{9}$",phno)
            if val1 and val2 and val3:
                return True
            else:
                return False

        obj1.idata(name,address,phno,cindate,coutdate,rno)
        result=collection_name.insert_many(hotellist)
        print(result.inserted_ids)
        

    if(choice==2):
        result1=collection_name.find()
        for i in result1:
            hotelview.append(i)
        print(hotelview)
        hotelview.clear()

    if(choice==3):
        n=input("enter customer name: ")
        result2=collection_name.find({"name":n})
        for i in result2:
            print(i)

    if(choice==4):
        # address=input("enter the address : ")
        # name=input("enter the customer name to be update: ")
        result3=collection_name.update_many({"address":"banglore"}, {"$set": {"name":"anagha"}})
        print(result3)

    if(choice==5):
        na=input("enter the name to delete: ")
        d=collection_name.delete_one({"name":na})
        print(d)

    if(choice==6):
        result5=collection_name.find({"name":{"$gt":"e"}},{"_id":0})
        for i in result5:
            print(i)

    
    if(choice==7):
        result6=collection_name.find({"name":{"$lt":"b"}},{"_id":0})
        for i in result6:
            print(i)

    if(choice==8):
        result=collection_name.aggregate([{"$group":{"_id":"$phno","count":{"$sum":0}}}])#group item based on id here we used branch
        for i in result:
            print(i)  

    if(choice==9):
        break
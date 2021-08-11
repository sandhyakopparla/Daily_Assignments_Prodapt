
import logging,pymongo,validation1
try:
    def adddogdetail(dogName,dogId,dogAge,dogPrice):
            dict1={"dogName":dogName,"dogId":dogId,"dogAge":dogAge,"dogprice":dogPrice}
            return dict1

    def Dogdetails():
        client=pymongo.MongoClient("mongodb://localhost:27017")
        mydatabase=client["DogDb"]
        collection_name=mydatabase['dogs']
        # obj=DogDetails()
        doglist=[]
        doglist2=[]
        Price_list=[]
        Age_list=[]
        # bill=[]
        # if(__name__=="__main__"):     
        #     user_name=input("please enter your username:")
        #     pass_word=getpass.getpass(prompt='Please enter your password:')
        #     if user_name==username and pass_word==password:
        while True:
            print("1.add dog details")
            print("------------------------")
            print("2.view all dogs")
            print("------------------------")
            print("3.search a dog by name")
            print("------------------------")
            print("4.delete a dog by name")
            print("------------------------")
            print("5 update the dog name by id")
            print("------------------------")
            print("6.List of dogs whoes name start after some specific character")
            print("------------------------")
            print("7.Sort according to price")
            print("------------------------")
            print("8.finding oldest dog")
            print("------------------------")
            print("9.exit")
            print("------------------------") 
            choice=int(input("Enter your choice : "))
            
            if choice==1:
                dogName=input("Enter the dogname : ")
                dogId=int(input("Enter the dogId : "))
                
                dogAge=int(input("Enter the Age:"))
                dogPrice=int(input("Enter the dog price:"))
                a=(validation1.validate(dogName))
                if a:
                    data=adddogdetail(dogName,dogId,dogAge,dogPrice)
                    doglist.append(data)
                    result=collection_name.insert_many(doglist)
                    print(result.inserted_ids) 
                else:
                    logging.error("invalid data enter a valid data")
                    
            if choice==2:
                result=collection_name.find({},{"_id":0})
                for i in result:
                    doglist2.append(i)
                print(doglist2)
                doglist2.clear()
            if choice==3:
                name=input("Enter the dogName to search : ")
                result=collection_name.find({"dogName":name})
                for i in result:
                    print(i)
            if choice==4:
                name=input("Enter the dogName that you want to delete:")
                result=collection_name.delete_many({"dogName":name})
                print(result.deleted_count)
            if choice==5:
                DogId=int(input("Enter the dogId where u want to update:"))
                DogName=input("Enter the DogName update:")
                result=collection_name.update_one({"dogId":DogId},{"$set":{"dogName":DogName}})
                print(result.modified_count)
                
            if choice==6:
                
                result1=collection_name.find({"dogName":{"$gt":"Q"}},{"_id":0})
                for i in result1:
                    print(i)
            if choice==7:
                result=collection_name.find({},{"_id":0}).sort("dogprice")
                for i in result:
                    print(i)
            if choice==8:
                Age_list=collection_name.find({},{"_id":0}).sort("dogAge",-1)
                for i in Age_list:
                    print(i)
                    break
            
            if choice==9:
                break
except:
    logging.error("unable to connect")

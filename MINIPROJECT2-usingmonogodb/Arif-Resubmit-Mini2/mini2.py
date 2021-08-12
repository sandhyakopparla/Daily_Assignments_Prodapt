import pymongo,logging,re,time,smtplib
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydatabase= client["Mini1Db"]
Collection_name =mydatabase["minis1"]
Collection_name1=mydatabase["dish"]
clist=[]
menu=["dosa","idly","meat","Paneer","Roti"]
menudict=dict.fromkeys(menu,0)

class Customer:
    def addCustomer(self,name,mobileNumber,emailId,menudict):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"name":name,"mobileNumber":mobileNumber,"emailId":emailId,"menudict":menudict,"AddOn":current_time}
        clist.append(dict1)
        #clist.append(menudict)
        print(clist)
k=Customer()
def validate(name,mobileNumber,emailId):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        mobileNumber1=re.search("^(\+91)[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search( "[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)   
        if name1 and  mobileNumber1 and emailId1:
            return True
        else:
            return False  

while(True):
    print("1.Add Customer")
    print("2. view Customer")
    print("3.search customer using name")
    print("4.delete customer")
    print("5.update customer")
    print("6.sent mail to customer")
    print("7.Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        name = input("Enter the name of Customer:")
        mobileNumber=input("Enter the mobilenumber:")
        emailId=input("Enter the email:")
        if validate(name,mobileNumber,emailId):
            while(1):
                print("1.dosa")
                print("2.idly")
                print("3.meat")
                print("4.Paneer")
                print("5.Roti")
                option=int(input("enter your option:"))
                if option==1:
                    dish1=int(input("how many dosa u want:"))
                    menudict["dosa"]=menudict["dosa"]+dish1
                if option==2:
                    dish2=int(input("how many idly u want:"))
                    menudict["idly"]=menudict["idly"]+dish2
                if option==3:
                    dish3=int(input("how many meat u want:"))
                    menudict["meat"]=menudict["meat"]+dish3
                if option==4:
                    dish4=int(input("how many Paneer u want:"))
                    menudict["Paneer"]=menudict["Paneer"]+dish4
                if option==5:
                    dish5=int(input("how many Roti u want:"))
                    menudict["Roti"]=menudict["Roti"]+dish5  
                if option ==6:
                    break          
                #if validate(name,mobileNumber,emailId):
            k.addCustomer(name, mobileNumber, emailId,menudict)
            result = Collection_name.insert_many(clist)
            print(result.inserted_ids)
        else:

            print("Please enter correct infomation ")
            continue
                
    if choice==2:
        result = Collection_name.find()
        li=[]
        for i in result:
            li.append(i)
        print(li)
        #result.clear()
               
    if choice==3:
        p = input("enter the customer name")
        result1 = Collection_name.find({"name":p})
        li = []
        for i in result1:
            li.append(i)
        print(li)

    if choice==4:
        q= input('enter the customer name')
        result=Collection_name.delete_one({'name':q})
        print(result.deleted_count)

    if choice==5:
        name=input("enter the customer information u want to update")
        emailId=input("enter the customer email u want to update")
        result=Collection_name.update_one({"name":name},{"$set":{"emailId":emailId}})
        print("data has been modified")
        #print(result.modified_count)
    if choice==6:
        result=Collection_name.find({"name":name})
        result1=Collection_name1.find_one()
        for i in result:
            a=i['menudict']
            message1 = "Dosa " +str( a['dosa']*result1['dish1'])+ "\nidly" +str(a["idly"]*result1["dish2"])+ "\n meat" +str(a["meat"]*result1["dish3"])+  "\n Paneer" +str(a["Paneer"]*result1["dish4"]) + "\n Roti" +str(a["Roti"]*result1["dish5"])
            message1=message1+"\n Your bill "+str ((a['dosa']*result1['dish1'])+(a["idly"]*result1["dish2"])+(a["meat"]*result1["dish3"])+(a["Paneer"]*result1["dish4"])+(a["Roti"]*result1["dish5"]))
            message="Your total amount is " +str(message1)
            print(message)
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
            connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],message)
            connection.quit
            print("Mail sent successfully")
    if choice==7:
        break
              


import smtplib,pymongo
import validation1,logging
try:
    def bill():
        client=pymongo.MongoClient("mongodb://localhost:27017")
        mydatabase=client["DogDb"]
        collection_name=mydatabase['dogs']
        email=input("Enter the user email")
        a=validation1.validatemail(email)
        if a:
            bill=[]
            Id=int(input("Enter the dogId that to generate bill:"))
            bill=collection_name.find({"dogId":Id})
            
            for i in bill:
                price=i["dogprice"]
            print(price)
            message="Thank you"+"\n your total amount is:"+str(price)+"\nTake care..Visit again"
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("kanchu954@gmail.com","Kanchu@8+")
            connection.sendmail("kanchu954@gmail.com",email,message)
            print("Email is successfully sent")
            connection.quit()
            collection_name.delete_one({"dogId":Id})
        else:
            logging.error("Enter a valid email")
except:
    logging.error("unable to process")
finally:
    print("Welcome..to..PetDog..Management...System")



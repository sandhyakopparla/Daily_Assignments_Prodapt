from pyzbar.pyzbar import decode
import csv,cv2,pymongo,smtplib,re,logging
from datetime import datetime,date
logging.basicConfig(filename='Bus1.log',level=logging.DEBUG)
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydata=client["Busdb"]
Registrationcollection=mydata["Registration"]
locationcollection=mydata["Location"]
ticketcollection=mydata["Ticket"]

def validation(firstname,lastname,username,password,number):
    valfname=re.search("^[A-Z]{1}[a-z]{0,25}$",firstname)
    vallame=re.search("^[A-Z]{1}[a-z]{0,25}$",lastname)
    valemail=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",username)
    valnumber=re.search("^(\+91)[6-9]\d{9}$",number)
    logging.info("Validation completed")
    if valemail and valfname and valnumber and vallame:
        return True
class Bus:
    def registration(self):
        firstname=input("Enter the First name: ")
        lastname=input("Enter the Last name: ")
        username=input("Enter the Email : ")
        password=input("Enter the password: ")
        number=input("Enter the Number : ")
        if  validation(firstname,lastname,username,password,number)==True:
            registrationlist=[]
            dictionary1={"firstname":firstname,"lastname":lastname,"username":username,"password":password,"number":number}
            registrationlist.append(dictionary1)
            result=Registrationcollection.insert_one(dictionary1)
            logging.info("Registration is completed added to database")

            print(result)
    def login(self,username,password):
        registrationresult=Registrationcollection.find()
        t=0
        bookedtickets=[]
        for i in registrationresult:
            if i["username"]==username and i["password"]==password:
                logging.info("Login is successful")

                while(1):
                    print("1) Book a ticket")
                    print("2) show the booked history")
                    print("3) Break")
                    option=int(input("Enter your choice :"))
                    if option==1:
                        cap = cv2.VideoCapture(0)
                        cap.set(3, 640)
                        cap.set(4, 480)
                        t = 0
                        while True:
                            success, img = cap.read()
                            for barcode in decode(img):
                                print(barcode.data)
                                mydata = barcode.data.decode('utf-8')
                                print(mydata)
                                if len(mydata) > 0:
                                    t = 1
                                    break
                            if t == 1:
                                break
                            cv2.imshow('Result', img)
                            cv2.waitKey(1)
                        details=locationcollection.find()
                        for j in details:
                            if mydata==j['source']:
                                print("1) pondicherry, Amount = 100")
                                print("2) Mahabalipuram, Amount = 200")
                                print("3) Chennai Amount, = 300")
                                choice=input("Enter Your Destination : ")
                                destination=j[choice]
                                print(destination)
                                day = str(date.today())
                                now = datetime.now()
                                time = str(now.strftime("%H:%M:%S"))
                                dict1={"name":i["firstname"]+" "+i["lastname"],"source":j["source"],"destination":destination['stop']
                                ,"price":destination['price'],"date":day,"time":time}
                                print(dict1)
                                bookedtickets.append(dict1)
                                break
                        print(bookedtickets)
                        ticketresult=ticketcollection.insert_many(bookedtickets)
                        print(ticketresult)
                        bookedtickets=[]
                        logging.info("Ticket is booked")

                        print(ticketcollection)
                        message="hi"+i["firstname"]+" "+i["lastname"]+" Your ticket is given below\n"+str(dict1)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("balu08062000@gmail.com","balu@123")
                        connection.sendmail("balu08062000@gmail.com",i["username"],message)
                
                        connection.quit
                    elif option==2:
                        names=i["firstname"]+" "+i["lastname"]
                        tickets=ticketcollection.find({"name":names})
                        for i in tickets:
                            print(i)
                    else:
                        break
        if t==0:
           print("print invalid details")
obj1=Bus()
try:
    while(1):
        print("Bus Booking Application : ")
        print("1) Registration")
        print("2) Login")
        print("3 Exit")
        choice=int(input("Enter the Choice: "))
        if choice==1:
            obj1.registration()
        elif choice==2:
            username=input("Enter the Username: ")
            password=input("Enter the Password: ")
            obj1.login(username,password)
        else:
            break
except:
    print("Some thing went wrong")
    logging.error("some thing went wrong")
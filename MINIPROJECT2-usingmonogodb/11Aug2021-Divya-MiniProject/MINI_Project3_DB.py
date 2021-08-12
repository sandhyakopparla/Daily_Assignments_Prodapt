import csv
import re,logging,pymongo
import pandas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

client = pymongo.MongoClient("mongodb+srv://chediv_1998:Basketball9@cluster0.8vz0p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
mydata = client["ExportsDB"]
Collection_name = mydata["Exports"]
logging.basicConfig(filename = "Exports.log" ,level=logging.DEBUG)
headerContent = ["Full_coconut","Husked_coconut","Copra_coconut","Rate","country_name"
                    ,"purpose","Totoal_count","Total_Price","Export_month"]
coconut_details = [ ]
class Export_Coconut:
    def add_coco_details(self,full_count,Husked_count,Copra_coconut_count,rate_of_coconut,Tot,Total_Price):
        self.full_count= full_count
        self.Husked_count = Husked_count
        self.Copra_coconut_count=Copra_coconut_count
        self.rate_of_coconut = rate_of_coconut
        self.Tot = Tot
        self.Total_Price = Total_Price
class Total_rate(Export_Coconut):
    def Export_details(self,country_name,purpose,month_of_export):
        self.country_name=country_name
        self.purpose=purpose
        self.month_of_export= month_of_export
        details = {"Full_coconut":full_count,"Husked_coconut":Husked_count,"Copra_coconut":Copra_coconut_count,
                    "Rate":rate_of_coconut,"country_name":country_name,"purpose":purpose,"Totoal_count":Tot,"Total_Price":Total_Price,"Export_month":month_of_export}
        coconut_details.append(details)
TR = Total_rate()

while(True):
    print("1.ADD COCONUT DETAILS")
    print("2.ADD EXPORT DETAILS")
    print("3.TO SAVE DATA IN DATABASE")
    print("4.TO DELETE ANY DATA")
    print("5.TO UPDATE DATA")
    print("6.FETCH AND SAVE FILE")
    print("7.DISPLAY BY SEARCH NAME")
    print("8.VIEW ALL DATA")
    print("9.SEND QUERY MAIL TO PRODUCER")
    print("10.EXIT")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        full_count=int(input("Enter count of Full coconut: "))            
        Husked_count= int(input("Enter count of husked Coconut: "))
        Copra_coconut_count = int(input("Enter count of Copra coconut: "))
        rate_of_coconut=int(input("enter a rate of one coconut: "))
        Tot = full_count+Husked_count+Copra_coconut_count
        Total_Price = Tot*rate_of_coconut
        TR.add_coco_details(full_count,Husked_count,Copra_coconut_count,rate_of_coconut,Tot,Total_Price)

    if choice == 2:
        country_name= input("Enter country name to export: ")
        purpose = input("Enter purpose of coconuts: ")
        month_of_export = input("enter Date & Month to export: ")
        TR.Export_details(country_name,purpose,month_of_export)

    if choice == 3:  
        Collection_name.insert_many(coconut_details)
        print(coconut_details)   
                
    if choice == 4:
        n = input("Enter name to delete data : ")
        result = Collection_name.delete_one({"country_name":n})
        print(result.deleted_count)
        
    if choice == 5:
        print("To update")
        c_name= input("Enter country name to export: ")
        purpose_update = input("Enter purpose of coconuts: ")
        month = input("enter Date & Month to export: ")
        result = Collection_name.update_one({"country_name":"USA"},{"$set":{"country_name":c_name,"purpose":purpose_update,"Export_month":month}})
        
    if choice == 6:
        result = Collection_name.find({},{'_id':0})
        Emp_details=[ ]
        for i in result:
            Emp_details.append(i)
        print(Emp_details) 
        with open('Export_Details.csv','w+',encoding='UTF8',newline='') as c:
            writer = csv.DictWriter(c,fieldnames=headerContent)
            writer.writeheader()
            writer.writerows(Emp_details)
        d = pandas.read_csv('Export_Details.csv')
        print(d)
    if choice == 7:
        name = input("Enter name of Country to search details: ")
        result = Collection_name.find({"country_name":name})
        for i in result:
            print(i)
    if choice == 8:
        result = Collection_name.find({ },{"_id":0})
        for i in result:
            print(i)

    if choice == 9:
        mail_id = input("Enter Producer Mail Id: ")
        va = re.search("r^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",mail_id)
        if va :
            print("valid email id")
        try:
            mail_content = ''' Dear producer,
                We got a tender to exports Goods(COCONUTS) from INDIA to USA and DUBAI.For that we need number of 
                coconuts.For your reference we attached document along with this mail for details of Goods.
                Thanking You,
                Yours Regards
                KSM Exports'''

            sender_address = 'Chedivya1998@gmail.com'
            sender_pass = 'Welcome@2169'
            receiver_address = mail_id

            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'Query For Exports-KSM Exports.'

            message.attach(MIMEText(mail_content, 'plain'))
            attach_file_name = 'Export_Details.csv'
            attach_file = open(attach_file_name, 'rb')
            # payload = MIMEBase('application', 'octate-stream')
            payload = MIMEBase('application', 'csv',Name=attach_file_name)
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload) 

            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)

            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print('Mail Sent')
        except:
            print("Value Error")
                   
    if choice == 10:
        print("Exit")
        logging.info("Program run successfully")
        print("Thank You")
        break
        









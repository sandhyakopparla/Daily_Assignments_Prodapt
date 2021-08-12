import smtplib,re,logging,json,time,csv,pymongo
from datetime import date

#########  Connection MongoDb
client=pymongo.MongoClient("mongodb://localhost:27017/")  
mydatabase=client["vaccinatedataDb"]
collection_name=mydatabase["vaccinate"]
try:
    print("############    VACCINATION MANAGEMENT SYSTEM     #############")
    vaccinatelist=[]
    logging.basicConfig(filename='vaccinate.log',level=logging.DEBUG)
    class Patient:
        def __init__(self,name,age,mbl_no,mail_id,gender,address,proof_name,proof_no,vaccinate,slot_date):
            self.name=name
            self.age=age
            self.mbl_no=mbl_no
            self.mail_id=mail_id
            self.gender=gender
            self.address=address
            self.proof_name=proof_name
            self.proof_no=proof_no
            self.vaccinate=vaccinate
            self.slot_date=slot_date

    class resultPatient(Patient):
        def __init__(self,name,age,mbl_no,mail_id,gender,address,proof_name,proof_no,vaccinate,slot_date,vaccine_count,vaccine_name,vaccinated_by,vaccinated_place):
            super().__init__(name,age,mbl_no,mail_id,gender,address,proof_name,proof_no,vaccinate,slot_date)
            self.vaccine_count=vaccine_count
            self.vaccine_name=vaccine_name
            self.vaccinated_by=vaccinated_by
            self.vaccinated_place=vaccinated_place
            dict={"name":name,"age":age,"mbl_no":mbl_no,"mail_id":mail_id,"gender":gender,"address":address,"proof_name":proof_name,"proof_no":proof_no,"vaccinate":vaccinate,"slot_date":slot_date,"vaccine_count":vaccine_count,"vaccine_name":vaccine_name,"vaccinated_by":vaccinated_by,"vaccinated_place":vaccinated_place}
            vaccinatelist.append(dict)
            
    ############ Validation
    def validate(vname,vmobile_number,vemail_id):
        name1=re.search("^[A-Z]{1}[a-z]{0,25}$",vname)
        print(name1)
        mobilenumber1=re.search("^91[6-9]\d{9}$",vmobile_number)
        print(mobilenumber1)
        emailid1=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",vemail_id)
        print(emailid1)
        if name1 and mobilenumber1 and emailid1:
            return True
        else:
            return False

    if __name__== "__main__":
        while(1):
            print("1.Add Patient Details")
            print("2.View all the patient Details")
            print("3.View the Today Vaccine Patient Details Using Slot Booking")
            print("4.Search the Patient Name")
            print("5.Update the Details")
            print("6.Delete the Details")
            print("7.Previous Vaccinate Count")
            print("8.Send all Patient Details for Mail")
            print("9.Exit")
            option=int(input("Enter Your Option:"))
            if option==1:
                vname=input("Enter the Patient Name:")
                age=input("Enter the Patient Age:")
                vmobile_number=input("Enter the Patient Mobile Number:")
                vemail_id=input("Enter the Patient EmailId:")
                gender=input("Enter the Patient Gender:")
                address=input("Enter the Patient Address:")
                proof_name=input("Enter the Patient Proof Name:")
                proof_no=input("Enter the Patient Proof Number:")
                vaccinate=input("Enter Previous Vaccinate(Yes or No):")
                slot_date=input("Enter the Vaccinate Slot Date:")
                vaccine_count=input("Enter the Vaccinate Count:")
                vaccine_name=input("Enter the Vaccinate Name:")
                vaccinated_by=input("Enter the Vaccinate By:")
                vaccinated_place=input("Enter the Vaccinate Place:")
                if validate(vname,vmobile_number,vemail_id):
                    obj=resultPatient(vname,age,vmobile_number,vemail_id,gender,address,proof_name,proof_no,vaccinate,slot_date,vaccine_count,vaccine_name,vaccinated_by,vaccinated_place)
                    collection_name.insert_many(vaccinatelist)
                    vaccinatelist=[]
                else:
                    logging.error("Wrong!Check Your Validation")

    ############ View all the patient Details Using JSON
            if option==2:
                r=collection_name.find()
                for i in r:
                    print(i)
                

    ############ View the Today Vaccine Patient Details Using Slot Booking
            if option==3:
                r=collection_name.find()
                vaccine=[]
                for i in r:
                    vaccine.append(i)
                current_time=time.localtime()
                tday=time.strftime("%d.%m.%Y",current_time)
                slot_date=(list(filter(lambda i:i["slot_date"]==str(tday),vaccine)))
                print(slot_date)
                logging.info("Today Vaccinate Sloting Details!!!")


    ############ Search the Patient Name
            if option==4:
                a=input("Search the Patient Name: ")
                r=collection_name.find({"name":a})
                for i in r:
                    print(i)
                    logging.info("Successfully!!! Search the data")

    ############ Update the Details
            if option==5:
                c=input("Enter Update Paitent Name:")
                update_age=input("Enter the Update Patient age:")      
                r=collection_name.update_many({"name":c},{"$set":{"age":update_age}})
                print(r)
                vaccinatelist.clear()
                logging.info("Successfully!!! update the data")

    ############ Delete the Details
            if option==6:
                b=input("Delete Patient Name:")
                r=collection_name.delete_many({"name":b})
                print(r.deleted_count)
                vaccinatelist.clear()
                logging.info("Successfully!!! delete the data")


    ############ Check Previous Count
            if option==7:
                r=collection_name.aggregate([{"$group":{"_id":"$vaccinate","count":{"$sum":1}}}])
                for i in r:
                    print(i)

                
    ############ Send all Patient Details for Mail
            if option==8:
                r=collection_name.find()
                vaccinate=[]
                for i in r:
                    vaccinate.append(i)
                    for x in vaccinate:
                        message="COVID VACCINATION DETAILS\n"+str(x)
                        print(message)
                        connection=smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("tamilarasiiprimed@gmail.com","Iprimed@123")
                        connection.sendmail("tamilarasiiprimed@gmail.com",x["mail_id"],message)
                        connection.quit
                        print("Mail Sent Successfully:)")

            if option==8:
                break
except ValueError:
    logging.error("Please Check Value int or string")

except IndexError:
    logging.error("Please Check Your Index")

except Exception:
    logging.error("Something Went Wrong")

finally:
    print("Äll Block Completed Successfully")





        

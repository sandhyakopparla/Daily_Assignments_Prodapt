import re,csv,logging,smtplib
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['registrationDb']
collection_name=mydatabase['registrations']
participants_list=[]
new_list=[]
try:
    headerContent=["name","roll","college","mailid","exam_type","fee","reg_date","reg_closing_date"]
    class ExamRegistration:
        def addParticipants(self,name,roll,college,mailid,exam_type,fee,reg_date,reg_closing_date):
            dict={"name":name,"roll":roll,"college":college,"mailid":mailid,"exam_type":exam_type,"fee":fee,"reg_date":reg_date,"reg_closing_date":reg_closing_date}
            participants_list.append(dict)
            return dict
    obj=ExamRegistration()
    def validation(name,roll,mailid):
        val1=re.match("[a-z]{2,20}$",name)
        val2=re.match("^[0-9]{0,7}$",roll)
        val3=re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",mailid)
        if val1 and val2 and val3:
            return True
        else:
            return False

    while(1):
        print("1.add participants")
        print("2.view all participants")
        print("3.search the  participant by name")
        print("4.list all the participants who registered first")
        print("5.save to csv file")
        print("6.delete participant")
        print("7.update participant")
        print("8.details sent to email")
        print("9.exit")
        
        choice=int(input("enter your choice:"))

        if choice==1:
            while(True):
                name=input("Enter the name:")
                roll=input("Enter the rollno:")
                mailid=input("Enter the mailid:")
                if validation(name,roll,mailid):
                    college=input("Enter the college name:")
                    exam_type=input("Enter the type of exam:")
                    fee=input("enter the amount:")
                    reg_date=input("Enter the registration date:")
                    reg_closing_date=input("Enter the registration closing date:")
                    obj.addParticipants(name,roll,college,mailid,exam_type,fee,reg_date,reg_closing_date)
                    result=collection_name.insert_many(participants_list)
                    print(result.inserted_ids)
                else:
                    print("please enter valid details")
                    continue
                break

        if choice==2:
            #print(participants_list)
            result=collection_name.find()
            for i in result:
                new_list.append(i)
                print(i)
                new_list.clear()

        if choice==3:
            # pname=input("Enter the name to search:")
            # print(list(filter(lambda i:i["name"]==pname,participants_list)))
            n=input("enter the rollno:")
            k=collection_name.find({"roll":n})
            for i in k:
                print(i)

        if choice==4:
            print("list all the participants who registered first:")
            print(sorted(participants_list,key=lambda i:i["reg_date"]))

        if choice==5:
            with open("Registration.csv","w+",encoding="UTF8",newline=" ") as r:
                writer=csv.DictWriter(r,fieldnames=headerContent)
                writer.writeheader()
                writer.writerows(new_list)

        if choice==6:
            pname=input("enter the name:")
            result=collection_name.delete_one({"name":pname})
            print(result.deleted_count)
        if choice==7:
            pnames=input("enter the participant name you have to update:")
            prollno=input("enter rollno:")
            pcollege=input("enter the college:")
            result=collection_name.update_one({"name":pnames},{"$set":{"roll":prollno,"college":pcollege}})
            print(result)

        if choice==8:
            email=input("enter the mailid:")
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("969kiran969@gmail.com","Kiran@969")
            message="your registration is successfully completed"
            connection.sendmail("969kiran969@gmail.com",email,message)
            print("email sent successfully")
            connection.quit()

        if choice==9:
            break

except Exception:
    logging.error("something went wrong")
finally:
    print("completed")
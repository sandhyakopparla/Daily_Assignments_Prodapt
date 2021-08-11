import re,csv,logging,pymongo,smtplib
donorlist=[]
patientlist=[]
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['BloodbankmgtDb'] #database
    collection_name=mydatabase['Blood bank management-D']
    collection_name1=mydatabase['Blood bank management-P']
    class BloodBankMgt:
            def donor(self,dname,did,dmail,dphno,daddress,dage,dbgroup):
                self.dname=dname
                self.did=did
                self.dmail=dmail
                self.dphno=dphno
                self.daddress=daddress
                self.dage=dage
                self.dbgroup=dbgroup
            def patient(self,pname,pid,pphno,paddress,page,pbgroup):
                self.pname=pname
                self.pid=pid
                self.pphno=pphno
                self.paddress=paddress
                self.page=page
                self.pbgroup=pbgroup   
            def adddonordetail(self,dname,did,dmail,dphno,daddress,dage,dbgroup):
                dict1={"dname":dname,"did":did,"dmail":dmail,"dphno":dphno,"daddress":daddress,"dage":dage,"dbgroup":dbgroup} 
                # print(dict1)
                return dict1
            def addpatientdetail(self,pname,pid,pphno,paddress,page,pbgroup):
                dict2={"pname":pname,"pid":pid,"pphno":pphno,"paddress":paddress,"page":page,"pbgroup":pbgroup} 
                # print(dict2)
                return dict2
    def validated(dname,did,dphno,daddress):
        valdonorname=re.search("^[A-Z]{1}[A-Z]{0,25}$",dname)
        valdid=re.search("^[0-9]{1,3}$",did)
        valdphno=re.search("^[7-9][0-9]{9}$",dphno)
        valdaddress=re.search("^[A-Z]{1}[A-Z]{0,200}$",daddress)
        valdbgroup=re.search("^[A-Z]{1,2}[+]|[-]$",dbgroup)
        if valdonorname and valdid and valdphno and valdaddress:
            return True
        else:
            return False    
    def validatep(pname,pid,pphno,paddress):
        valpatientname=re.search("[A-Z]{1}[A-Z]{0,25}$",pname)
        valpid=re.search("[0-9]{1,3}$",pid)
        valpphno=re.search("^[7-9][0-9]{9}$",pphno)
        valpaddress=re.search("[A-Z]{1}[A-Z]{0,200}$",paddress)
        if valpatientname and valpid and valpphno and valpaddress:
            return True
        else:
            return False
    obj=BloodBankMgt()
    if(__name__=="__main__"):
        while True:
            print("1.Add Donor details")
            print("2.Display Donor details") 
            print("3.Search Donor by ID")
            print("4.Delete Donor by ID")
            print("5.Update Donor name by DONOR ID")
            print("6.Add patient details")
            print("7.Display Patient details")
            print("8.Search Patient based on ID")
            print("9.Delete Patient by ID")
            print("10.Update Patient age based on ID")
            print("11.Send mail to Donor about the requirement :")
            print("12.Exit")
            choice=int(input("Enter your option : "))
            if choice==1:
                dname=input("Enter the DONOR NAME : ") 
                did=input("Enter the DONOR ID : ") 
                dmail=input("Enter the DONOR MAIL ID : ") 
                dphno=input("Enter the DONOR PH NO : ")
                daddress=input("Enter the DONOR ADDRESS : ")
                dage=input("Enter the DONOR AGE : ")
                dbgroup=input("Enter the DONOR Blood GROUP : ")
                if validated(dname,did,dphno,daddress)==True:
                    data=obj.adddonordetail(dname,did,dmail,dphno,daddress,dage,dbgroup) 
                    donorlist.append(data)
                    result=collection_name.insert_many(donorlist)
                    print(result.inserted_ids)
                else:
                    logging.error("VALIDATION ERROR!!!")
                    break
            if choice==2:
                result= collection_name.find({},{"_id":0}) 
                donorlist=[]
                for i in result:
                    donorlist.append(i)
                print(donorlist)
                
            if choice==3:
                sea=input("Enter the DONOR ID :")
                result= collection_name.find({"did":sea},{"_id":0}) 
                for j in result:
                    print(j)
                donorlist.clear()    
            if choice==4:
                de=input("Enter the DONOR ID :")
                result= collection_name.delete_many({"did":de}) 
                print(result)         
            if choice==5:
                s=input("Enter the DONOR ID :")
                t=input("Enter the DONOR NAME to be updated")
                result= collection_name.update_one({"did":s},{"$set":{"dname":t}})
                print(result)        
            if choice==6:
                pname=input("Enter the PATIENT NAME : ") 
                pid=input("Enter the PATIENT ID : ") 
                pphno=input("Enter the PATIENT PH NO : ")
                paddress=input("Enter the PATIENT ADDRESS : ")
                page=input("Enter the PATIENT AGE : ")
                pbgroup=input("Enter the PATIENT Blood GROUP : ")
                if validatep(pname,pid,pphno,paddress)==True:
                    data1=obj.addpatientdetail(pname,pid,pphno,paddress,page,pbgroup) 
                    patientlist.append(data1)
                    result=collection_name1.insert_many(patientlist)
                    print(result.inserted_ids)
                else:
                    logging.error("VALIDATION ERROR!!!")
                    break
            if choice==7:
                result= collection_name1.find({},{"_id":0}) 
                patientlist=[]
                for i in result:
                    patientlist.append(i)
                print(patientlist)
                patientlist.clear()
            if choice==8:
                sea=input("Enter the PATIENT ID :")
                result= collection_name1.find({"pid":sea},{"_id":0}) 
                for j in result:
                    print(j)
            if choice==9:
                de=input("Enter the PATIENT ID :")
                result= collection_name1.delete_many({"pid":de}) 
                print(result) 
            if choice==10:
                s=input("Enter the PATIENT ID :")
                t=input("Enter the PATIENT AGE to be updated")
                result= collection_name1.update_one({"pid":s},{"$set":{"page":t}})
                print(result)    
            if choice==11:
                getmail=input("Enter donor mail ID : ")
                msg= "We are glad to know about your interest in donating blood \n\nThere is an requirement now please reach out to us. \n\n\n\nTHANK YOU!!"
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("rakesh.learning.python@gmail.com","9008496668Ra@")
                connection.sendmail("rakesh.learning.python@gmail.com",getmail,msg)
                print("EMAIL SENT")
                connection.quit()
                 
            if choice==12:
                break    
except:
    logging.error("OOPS!! Something is wrong") 
finally:
    print("Thank you")                                                                      
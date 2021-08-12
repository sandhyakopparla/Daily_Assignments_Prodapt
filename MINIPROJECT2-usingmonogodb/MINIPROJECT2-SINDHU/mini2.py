import csv
import re
import logging
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection 
mydatabase=client['ElectionDb'] #database
collection_name=mydatabase['election'] #collection
collection_name1=mydatabase['vote']

candidatelist = []
voterlist = []
headerContent1 = ["candname", "candgender","candaddress", "candparty", "candcity","_id"]
headerContent2 = ["votid", "votname", "votwardno", "votaddress", "votphoneno","_id"]

try:
    class ElectionManagement:
        def candidate(self, candname, candgender, candaddress, candparty, candcity):
            self.candname = candname
            self.candgendr = candgender
            self.candaddress = candaddress
            self.candparty = candparty
            self.candcity = candcity

        def voter(self, votname, votid, votwardno, votaddress, votphoneno):
            self.votid = votid
            self.votname = votname
            self.votwardno = votwardno
            self.votaddress = votaddress
            self.votphoneno = votphoneno

        def addcandidatedetails(self, candname, candgender, candaddress, candparty, candcity):
            dict1 = {"candname": candname, "candgender": candgender,
                    "candaddress": candaddress, "candparty": candparty, "candcity": candcity}
            
            result=collection_name.insert_one(dict1)
            print(result)
            return dict1

        def addvoterdetails(self, votname, votid, votwardno, votaddress, votphoneno):
            dict2 = {"votname": votname, "votid": votid, "votwardno": votwardno,
                    "votaddress": votaddress, "votphoneno": votphoneno}
            voterlist.append(dict2)
            result=collection_name1.insert_many(voterlist) 
            return dict2

    def validate(candname, candgender, candaddress, candparty, candcity):
        valcandname = re.search("^[A-Z]{1}[A-Z]{0,25}$", candname)
        valcandaddress = re.search("^[A-Z]{1}[A-Z]{0,200}$", candaddress)
        valcandparty = re.search("^[A-Z]{1}[A-Z]{0,25}$", candparty)
        valcandcity = re.search("^[A-Z]{1}[A-Z]{0,200}$", candcity)
        valcandgender = re.search("FEMALE|MALE", candgender)
        if valcandname and valcandaddress and valcandparty and valcandcity and valcandgender:
            return True
        else:
            return False


    def validatevote(votname, votid, votwardno, votaddress, votphoneno):
        valvotname = re.search("[A-Z]{1}[A-Z]{0,25}$", votname)
        valvotid = re.search("[0-9]{1,3}$", votid)
        valvotwardno = re.search("[0-9]{1,3}$", votwardno)
        valvotaddress = re.search("[A-Z]{1}[A-Z]{0,200}$", votaddress)
        valvotphoneno = re.search("^[7-9][0-9]{9}$", votphoneno)
        if valvotname and valvotid and valvotwardno and valvotaddress and valvotphoneno:
            return True
        else:
            return False


    obj = ElectionManagement()

    while True:
        print("1)enter Candidate details")
        print("2)Search Candidate by party name")
        print("3)Save to file")
        print("4)enter Voter details")
        print("5)Search Voter by ID")
        print("6)Save to file")
        print("7)Exit")
        choice = int(input("Enter your option : "))
        if choice == 1:
            candname = input("Enter the candidate name : ")
            candgender = input("Enter candidate gender : ")
            candaddress = input("Enter candidate address : ")
            candparty = input("Enter candidate party : ")
            candcity = input("Enter candidate city : ")
            if validate(candname, candgender, candaddress, candparty, candcity):
                obj = ElectionManagement()
                obj.candidate(candname, candgender,
                            candaddress, candparty, candcity)
                candidatelist.append(obj.addcandidatedetails(candname, candgender, candaddress, candparty, candcity))
            else:
                logging.error("invalid data enter a valid data")

        if choice == 2:
            candparty1 = input("Enter the party to search : ")
            result=collection_name.find({'candparty':candparty1})
            for i in result:
                print(i)
            #print(list(filter(lambda i: i["candparty"] == candparty, candidatelist)))

        if choice == 3:
            with open('candidate.csv', 'a+', encoding='UTF8', newline='') as s:
                print(candidatelist)
                writer = csv.DictWriter(s, fieldnames=headerContent1)
                writer.writeheader()
                writer.writerows(candidatelist)

        if choice == 4:
            votname = input("Enter voter name: ")
            votid = input("Enter voter ID : ")
            votwardno = input("Enter voter wardno : ")
            votaddress = input("Enter voter address : ")
            votphoneno = input("Enter voter phoneno : ")
            if validatevote(votname, votid, votwardno, votaddress, votphoneno):
                obj.voter(votname, votid, votwardno, votaddress, votphoneno)
                obj.addvoterdetails(
                    votname, votid, votwardno, votaddress, votphoneno)
                print(voterlist)
            else:
                logging.error("invalid data enter a valid data")

        if choice == 5:
            votid1 = input("Enter the voterid to search : ")
            result=collection_name.find({'votid':votid1})
            for i in result:
                print(i)
            #print(list(filter(lambda i: i["votid"] == votid, voterlist)))

        if choice == 6:
            with open('voter.csv', 'a+', encoding='UTF8', newline='') as s:
                writer = csv.DictWriter(s, fieldnames=headerContent2)
                writer.writeheader()
                writer.writerows(voterlist)

        if choice == 7:
            print("Exit")
            break

    
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")
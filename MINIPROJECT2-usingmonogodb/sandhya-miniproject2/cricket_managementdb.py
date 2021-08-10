import re,csv,logging,json,pymongo
from valibat import validation_of_batsman
from valibow import validation_of_bowler
from valiall import validation_of_allrounder
# from collections import deque
Battinglist=[]
Bowlerlist=[]
all_rounderlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['CricketDb']
collection_name=mydatabase['cricketers']
try:
    class Cricketers:
        def bats(self,batsman_name,matchone_score,matchtwo_score,b_location):
            self.batsman_name=batsman_name
            self.matchone_score=matchone_score
            self.matchtwo_score=matchtwo_score
            self.b_location=b_location
        def bowler(self,bowler_name,bo_location):
            self.bowler_name=bowler_name 
            self.bo_location=bo_location
        def allrounder(self,all_roundername,all_location):
            self.all_roundername=all_roundername
            self.all_location=all_location
        def addbatsdetails(self):
            match_score=matchone_score+matchtwo_score
            dict1={"match_score":match_score,"batsman_name":batsman_name,"matchone_score":matchone_score,"matchtwo_score":matchtwo_score,"b_location":b_location}
            Battinglist.append(dict1)
            # print(Battinglist)
        def addbowlerlist(self):
            dict2={"bowler_name":bowler_name,"bo_location":bo_location}
            Bowlerlist.append(dict2)
        def addallrounderlist(self):
            dict3={"all_roundername":all_roundername,"all_location":all_location}
            all_rounderlist.append(dict3)
    obj1=Cricketers()
    while(True):
        print("\n enter your choice:")
        print("1.Add batsman")
        print("2.store the  batsman details in db")
        print("3.Add Bowlers:")
        print("4.store the bowlers details in db")
        print("5.Add All rounders")
        print("6.store All rounder details in db")
        print("7.search for the particular person in a batsmanlist")
        print("8.update the details")
        print("9.delete")
        print("10.Exit") 
        choice=int(input("enter your choice:"))
        if choice==1:
            batsman_name=input("enter the name of the bats_man - ")
            matchone_score=int(input("enter the score of matchone_score - "))
            matchtwo_score=int(input("enter the matchtwo_score - "))
            b_location=input("enter the location")
            if validation_of_batsman(batsman_name,b_location):
                obj1=Cricketers()
                obj1.bats(batsman_name,matchone_score,matchtwo_score,b_location)
                obj1.addbatsdetails()
                # print(Battinglist)
                result=collection_name.insert_many(Battinglist)
                print(result.inserted_ids)
            else:
                print("please enter valid details")
        if choice==2:
            result=collection_name.find({},{"_id":0})
            print(result)
            Battingtlist=[]
            for i in result:
                Battinglist.append(i)
                print(Battinglist)
        if choice==3:
            bowler_name=input("enter the bowler name - ")
            bo_location=input("enter the b_location")
            if validation_of_batsman(bowler_name,bo_location):
                obj1.bowler(bowler_name,bo_location)
                obj1.addbowlerlist()
                result=collection_name.insert_many(Bowlerlist)
                print(result.inserted_ids)
            else:
                print("please enter valid details")
        if choice==4:
            result=collection_name.find({},{"_id":0})
            Bowlerlist=[]
            for i in result:
                Bowlerlist.append(i)
            print(Bowlerlist)
        if choice==5:
            all_roundername=input("enter the allrounder name -")
            all_location=input("enter the location - ")
            if validation_of_batsman(all_roundername,all_location):
                obj1.allrounder(all_roundername,all_location)
                obj1.addallrounderlist()
                result=collection_name.insert_many(all_rounderlist)
                print(result.inserted_ids)
        if choice==6:
            result=collection_name.find({},{"_id":0})
            all_rounderlist=[]
            for i in result:
                all_rounderlist.append(i)
                print(all_rounderlist)
        if choice==7:
            result=collection_name.find({"batsman_name":"shikardawan"})
            print(result)
            Battinglist=[]
            for i in result:
                Battinglist.append(i)
            print(Battinglist)
        if choice==8:
            result=collection_name.update_one({"batsman_name":"shikardawan"},{"$set":{"b_location":"jarkhand"}})
            print(result)
        if choice==9:
            result=collection_name.delete_one({"bowler_name":"jadeja"})
            print(result)
        if choice==10:
            break
except:
    logging.error("invalid details")
finally:
    print("thankyou!")

    
    
    
    
       
    
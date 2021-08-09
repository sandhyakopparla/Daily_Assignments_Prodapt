import re,csv,logging,json
from valibat import validation_of_batsman
from valibow import validation_of_bowler
from valiall import validation_of_allrounder
# from collections import deque
Battinglist=[]
Bowlerlist=[]
all_rounderlist=[]
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
            print(Battinglist)
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
        print("2.Display batsman details in json")
        print("3.Add Bowlers:")
        print("4.Dipplay Bowler details in json")
        print("5.Add All rounders")
        print("6.display All rounder details in json")
        print("7.search for the particular person in a batsmanlist")
        print("8.Ranking according to their score avg and also save in json file")
        print("9.Exit") 
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
            else:
                print("please enter valid details")
        if choice==2:
            myjson=json.dumps(Battinglist)
            with open("Batting_api.json","w",encoding="utf-8") as b:
                b.write(myjson)
        if choice==3:
            bowler_name=input("enter the bowler name - ")
            bo_location=input("enter the b_location")
            if validation_of_batsman(bowler_name,bo_location):
                obj1.bowler(bowler_name,bo_location)
                obj1.addbowlerlist()
            else:
                print("please enter valid details")
        if choice==4:
            myjson=json.dumps(Bowlerlist)
            with open("Bowler_api.json","w",encoding="utf-8") as ba:
                ba.write(myjson)
        if choice==5:
            all_roundername=input("enter the allrounder name -")
            all_location=input("enter the location - ")
            if validation_of_batsman(all_roundername,all_location):
                obj1.allrounder(all_roundername,all_location)
                obj1.addallrounderlist()
        if choice==6:
            myjson=json.dumps(all_rounderlist)
            with open("all_rounder_api.json","w",encoding="utf-8") as al:
                al.write(myjson)
        if choice==7:
            cricketer=input("enter the name to search")
            print(list(filter(lambda i:i["batsman_name"]==cricketer,Battinglist)))
        if choice==8:
            rank=sorted(Battinglist,reverse=True,key=lambda i:i["match_score"])
            myjson=json.dumps(rank)
            with open("Cricketerscore_api.json","w",encoding="utf-8") as s:
                s.write(myjson)
        if choice==9:
            break
except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfuly")
finally:
    print("Thank you!!")
    

    
    
    
    
       
    
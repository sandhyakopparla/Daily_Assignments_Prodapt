import logging,getpass
import DogDetails
import GenrateBill
try:
    username="kanchana"
    password="Kanchana@8+"
    user_name=input("please enter your username:")
    pass_word=getpass.getpass(prompt='Please enter your password:')
    if user_name==username and pass_word==password:

        while True:

            print("\n1.Dog Details ")
            print("-------------------------")
            print("\n2.To generate bill")
            print("-------------------------")
            print("\n3.close")
            print("-------------------------")
            choice=int(input("Enter your choice:"))
            if choice==1:
                DogDetails.Dogdetails()
            if choice==2:
                GenrateBill.bill()
            if choice==3:
                break
except:
    logging.error("Something went wrong")
finally:
    print("Thank you for using")
        





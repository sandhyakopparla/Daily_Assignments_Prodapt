import re,logging
import smtplib
try:
    a = int(input('Enter the number of cup of TEA (0 if you don\'t want)  -  '))
    b = int(input('Enter the number of cup of COFFEE (0 if you don\'t want)  -  '))
    c = int(input('Enter the number of MASALA DOSA (0 if you don\'t want)  -  '))
    d = int(input('you have completed the order now press 4 to get your bill - '))
    email = input('Enter your email id:')
    emailid=re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)
    if emailid:
        Email=email
    connection=smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login("practicedigital12@gmail.com","sandhya9@9")
    if(d==4):
        message =a*7+b*10+c*50
    message=str(message)
    connection.sendmail("sandhyakopparla24@gmail.com",Email, message)
    connection.quit()
except Exception:
    logging.error("Your order is not in our menu")
else:
    print("your order amount is",message)
    print("Successfuly order placed") 
finally:
    print("Thank you for visiting our restaurant!")
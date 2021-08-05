import re,sys,datetime,csv,time
from datetime import date
import time
header=['productname','discription','price','manufacturer','manufacturingdate','expirydate']
productlist=[]
ti=time.localtime()
current_clock=time.strftime("%Y-%m-%d %H:%M:%S",ti)
class ProductDetails:
    # def Pro(self,productname,discription,price,manufacturer,manufacturingdate,expirydate):
    #     self.productname=productname
    #     self.discription=description
    #     self.price=price
    #     self.manufacturer=manufacturer
    #     self.manufacturingdate=manufacturerdate
    #     self.expirydate=expirydate
    def addproductdetails(self,productname,discription,price,manufacturer,manufacturingdate,expirydate):
        dict1={"productname":productname,"discription":discription,"price":price,"manufacturer":manufacturer,"manufacturingdate":manufacturingdate,"expirydate":expirydate}
        productlist.append(dict1)
obj1=ProductDetails()
today=datetime.date.today()
while(True):
    print("1.Add Products")
    print("2.View all products")
    print("3.Search a product")
    print("4.list all the products that expired today")
    print("5.exit")
    print("6.save the file")
    choice=int(input("enter your choice:"))
    if choice==1:
        productname=input("enter the product name")
        discription=input("enter the description of product")
        price=input("enter the price")
        manufacturer=input("enter the manufacturer name:")
        manufacturingdate=input("enter date in mm-dd-yyyy format")
        expirydate=input("enter the expiry date in mm-dd-yyyy format:")
        v=re.search("^[1-9]",price)
        if v:
            price=int(price)
        obj1.addproductdetails(productname,discription,price,manufacturer,manufacturingdate,expirydate)
    if choice==2:
        print(productlist)
    if choice==3:
        S=input("enter the product to search:")
        print(list(filter(lambda i:i["productname"]==S,productlist)))
    if choice==4:
        current_time=time.localtime()
        tday=time.strftime("%Y-%m-%d",current_time)
        # ed=time.strftime("%d-%m-%y")
        #today=datetime.date.today()
        
        expirylist=(list(filter(lambda i:i["expirydate"]==str(tday),productlist)))    
        if len(expirylist)>0:
            print(expirylist)
        else:
            print("No records found")
    if choice==6:
        with open('pro.csv','w+',encoding='UTF8',newline='') as p:
            writer = csv.DictWriter(p,fieldnames=header)
            writer.writeheader()
            writer.writerows(productlist)
    if choice==5:
        sys.exit()


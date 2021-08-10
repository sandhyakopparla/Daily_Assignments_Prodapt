import re,sys,logging
import pymongo
from valipro import validation_of_product
productlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase=client['ProductDb']
collection_name=mydatabase['products']
try:
    class Product:
        def addproductdetails(self):
            dict1={"productcode":productcode,"productname":productname,"distributor_name":distributor_name,"manufacturing_year":manufacturing_year,"retail_price":retail_price,"wholesale_price":wholesale_price,"product_discription":product_discription,"manufacturer_number":manufacturer_number}
            productlist.append(dict1)
    while(True):
        print("1.Add Products")
        print("2.View all products")
        print("3.Search a product")
        print("4.delete")
        print("5.update ")
        print("6.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            productcode=input("enter the productcode")
            productname=input("enter the product name")
            distributor_name=input("enter the distributor of product")
            manufacturing_year=input("enter year")
            retail_price=input("enter the retailprice")
            wholesale_price=input("enter the wholesale price")
            product_discription=input('enter the description')
            manufacturer_number=input("enter the number")
            if validation_of_product(productname,distributor_name,manufacturer_number):
               obj=Product()
               obj.addproductdetails()
               print(productlist)
               result=collection_name.insert_many(productlist)
               print(result.inserted_ids)
        if choice==2:
            result=collection_name.find({},{"_id":0})
            productlist=[]
            for i in result:
                productlist.append(i)
            print(productlist)
        if choice==3:
            result=collection_name.find({"productcode":"12"})
            print(result)
            productlist=[]
            for i in result:
                productlist.append(i)
            print(productlist)
        if choice==4:
        # result=collection_name.delete_many({"productcode":"sandhya"})#it is
            result=collection_name.delete_one({"productcode":"78"}) 
            print(result)
        if choice==5:
            result=collection_name.update_one({"poductcode":"78"},{"$set":{"productname":"natas"}})
            print(result)
        if choice==6:
            sys.exit()
except:
    logging.error("Invalid validation kindly check it")
else:
    logging.info("done!")

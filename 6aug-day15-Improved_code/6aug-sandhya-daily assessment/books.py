import re,csv,logging,json
from valimodule import validation_of_books
bookslist=[]
class Books:
    def booklist(self,book_title,author,description,price,distributor_name,publisher):
        self.book_title=book_title
        self.author=author
        self.description=description
        self.price=price
        self.distributor_name=distributor_name
        self.publisher=publisher
    def addbooklist(self):
        dict1={"book_title":book_title,"author":author,"description":description,"price":price,"distributor_name":distributor_name,"publisher":publisher}
        bookslist.append(dict1)
        obj1=Books()
while(True):
        print("1.Add Books")
        print("2.View all Books")
        print("3.view all the books_title in alphabetical order")
        print("4.search a book by title")
        print("5.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            book_title=input("enter the book name")
            author=input("enter the author")
            description=input("enter the description of product")
            price=input("enter the price")
            distributor_name=input("enter the distributor_name")
            publisher=input("enter the publisher")
            # if validation_of_books(book_title,author,description,price,distributor_name,publisher):
            obj1=Books()
            obj1.booklist(book_title,author,description,price,distributor_name,publisher)
            obj1.addbooklist()
            # else:
            #     print("please enter valid details")
        if choice==2:
            myjson=json.dumps(bookslist)
            with open("Books_api.json","w",encoding="utf-8") as b:
                b.write(myjson)
        if choice==3:
            book=sorted(bookslist,key=lambda i:i["book_title"])
            myjson=json.dumps(book)
            with open("book_api.json","w",encoding="utf-8") as b:
                b.write(myjson)
        if choice==4:
            book=input("enter the name to search")
            print(list(filter(lambda i:i["book_title"]==book,bookslist)))
        if choice==5:
            break







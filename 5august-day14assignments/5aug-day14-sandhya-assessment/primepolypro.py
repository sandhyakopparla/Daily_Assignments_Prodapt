import multiprocessing
def prime():
    lower=2
    upper=500
    for n in range(lower,upper+1):
        if n>1:
            for i in range(2,n):
                if(n%i)==0:
                    break
                else:
                    print(n,end=" ")
                    break
def polindrome():
    maximum=500
    for n in range(10,maximum+1):
        temp=n
        reverse=0
        while(temp>0):
            Remainder=temp%10
            reverse=(reverse*10)+Remainder
            temp=temp//10
        if(n==reverse):
            print(n,end=' ')
if(__name__=="__main__"):
    p1=multiprocessing.Process(target=prime)
    p2=multiprocessing.Process(target=polindrome)
    p1.start()
    p1.join()
    print("\n","done with prime")
    p2.start()
    p2.join()
    print("\n","done with palindrome")


#     p1=multiprocessing.(target=findsquare,args=(mylist,))
# p2=multiprocessing.(target=findcube,args=(mylist,))
# p1.start()
# p2.start()
# p1.join()
# p2.join()
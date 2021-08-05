import threading,time
def prime():
    lower=int(input("enter the lower value:"))
    upper=int(input("enter the upper value:"))
    for n in range(lower,upper+1):
        if n>1:
            for i in range(2,n):
                if(n%i)==0:
                    break
                else:
                    print(n,end=" ")
                    break
def polindrome():
    maximum=int(input("enter the maximum value:"))
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
    t1=threading.Thread(target=prime)
    t2=threading.Thread(target=polindrome)
    t1.start()
    t1.join()
    print("done with prime")
    t2.start()
    t2.join()
    print("done with palindrome")
import timeit
mylist=[10,24,45,22,11,88]
def f1():
    mylist.sort()
print(timeit.timeit(f1,number=100000)) 



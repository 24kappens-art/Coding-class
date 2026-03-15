def add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    result=a+b
    print("The sum is: ",result)
if __name__=="__main__":
    add() 

'''
def add(x,y):
    result=x+y
    print("The sum is: ",result)
if __name__=="__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    add(a,b)  
'''
def add(x,y):
    res1=x+y
    res2=x-y
    res3=x*y
    return res1,res2,res3
if __name__=="__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    r1,r2,r3=add(a,b)
    print(er1,r2,r3)      
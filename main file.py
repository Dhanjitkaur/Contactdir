'''
Main file
=========
'''
def vaildate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
    fp=open('data.txt','w')
    n=input("enter name:")
    mn=input("enter mobile number:")
    res=vaildate_mob(mn)
    #print(res)
    if res==1:
        a,b=searchmob(mn)
        if b==1:
            print("number already exist")
        else: 
          d=n+":"+mn+"\n"
          fp.write(d)
          fp.close()

          print("contact created successfully!!")
    else:
        print("please enter vaild number")

def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("============contact directory======")
    print()
    print(d)
    print("===============")

def searchmob(n):
        
        fp=open('data.txt','r')
        data=fp.readlines()
        for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("contact found:")
               # print(x)
                return x,1
            else:
                return '',0
                
def searchname():
       print("search contact number by name")
       ns=input("enter name:")
       fp=open('data.txt','r')
       data=fp.raedlines()
       #print(data)       
       flag=0
       for x in data:
               print(x)
               l=x.split(":")
               #print(l)
               #print(l[0])
               if ns.upper()==l[0].upper():
                   print(X)
                   flag=1
               if flag==0:
                 print("contact not found")
                 fp.close()
               
               
                
print("Welcome to contact directory console application")
print()
while True:
    print("1.create contact")
    print("2.view contacts")
    print("3.search by name")
    print("4.search by mobile number")
    print("5.Exit")
    ch=int(input("Enter your choice:"))
           
    if ch==1:
        create_contact()
    elif ch==2:
            display()
    elif ch==3:
            pass
    elif ch==4:
          ms=input("enter mobile number to be search:")
          a,b=searchmob(ms)
          print(a)
          print(b)
          if b==1:
              print("number is found:")
              print(a)
          else:
              print("not found")
    elif ch==5:
             break
    else:
                print("please enter vaild option!!!")
                
print("Thank you for using application")    

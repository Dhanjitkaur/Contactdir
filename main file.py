'''
main file
==========
'''



def validate_mob(x):
    if x.  isdigit() and len(x)==10:
        return 1
    else:
        return 0
def create_contact():
         fp=open('data.txt','a')
         n=input("Enter Name:")
         mn=input("Enter a mobile number:")
         res=validate_mob(mn)
         #print(res)
         if res==1:
             a,b=searchmob(mn)
             if b==1:
                 print("Number is already exit")
             else:
                 
                 d=n+":"+mn+"\n"
                 fp.write(d)
                 fp.close()
                 print("Contact created sucessfully")
         else:
            print("pleae enter valid mobile number")
def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("===============Contact Directory============")
    print()
    print(d)
    print("========================================")
def searchmob(n):
       
        fp=open('data.txt','r')
        data=fp.readlines()
        for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("Contact Found:")
                #print(x)
                
                return x,1
        else:
                return '',0
def searchname():
        print("Search contact Number by Name")
        ns=input("Enter name:")
        fp=open('data.txt','r')
        data=fp.readlines()
       # print(data)
        flag=0
        for x in data:
           # print(x)
           l=x.split(":")
           #print(l)
           #print(l[0])
           if ns.upper()==l[0].upper():
               
               print(x)
               flag=1
        if flag==0:
             print("Contact Not Found")
        fp.close()
      
    

print("welcome to contact Directory console Application")
print()
while True:
    print()
    print("1.create Contact")
      
    print("2.View Contacts")
    print("3.Search by name")
    print("4.Search by Mobile number")
    print("5.Exit")
    ch=int(input("Enter your Choice:"))


    if ch==1:
         create_contact()
         
         pass
    elif ch==2:
        display()
        
        pass
    elif ch==3:
        searchname()
    
        pass
    elif ch==4:
        ms=input("Enter mobile number to be searched:")
        a,b=searchmob(ms)
        #print(a)

        #print(b)
        if b==1:
            print("Number Found")
            print(a)
        else:
            print("Not Found")
       
        
        pass
    elif ch==5:
        break
    else:
        print("Please enter a valid option!!!")
    

        

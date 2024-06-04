
class Contacts:
    def __init__(self):
        print("CONTACT_LIST")
    #ADD THE INPUT VALUES
    def add(self,name,num):
        if name in con:
            print(f" Already there in contact with this number {con[name]}")

        dic[name]=num
        print("Add sucessfully")

    #SEARCH THE REQURIED CONTACT   
    def search(self,name):
        if name in con:
            print(f"{name}:{con[name]}")

        else:
            print(name,"Not in contacts checkgain")
    
    #DELETE THE VALUE
    def delete(self,name):
        if name  in con:
            con.pop(name)
            print(f"{name} is delet")
        else:
            print(name,"value is not there")

#PHONE_CONTACTS_DATA_STORE_IN_FILES

con={}
dic={}

#ACCESS THE DATA AND CONVERT INTO THE DICTIONARY
f1=open("file_path.txt","r")

lines=f1.readlines()
for i in lines:
    key,values=i.strip().split(":")
    con[key.strip()]=values.strip()


ob=Contacts()

#TAKING INPUTS AND RUN THE FUNCTIONS AS PER USER REQUIRED
while True:
    k=input("enter function a=add,s=search,d=delet,l=Contact_list,q=quit")
    if k=="a":
        name=input("enter the name")
        num=int(input("enter the number"))
        ob.add(name,num)
    elif k=="s":
        name=input("Enter the name for find")
        ob.search(name)
    elif k=="d":
        name=input("Enter the name delet")
        
        ob.delete(name)
    
    elif k=="l":
        print("CONTACTS")
        for i,j in con.items():
            print(f"{i}:{j}")

    elif k=="q":
        print("Thanks for using app visit again")
        break
    else:
        print("please read the instructions carefully")

#PASSING THE VALUES AND STORE IN PYTHON
fil=open("file_path.txt","a")
for i,j in dic.items():
    
    fil.write(f"{i}:{j}\n")
fil.close()

import csv
from datetime import date
from prettytable import *
import pandas as pd 
import os
if not os.path.exists('items.csv'):
     with open("items.csv", mode='w', newline='') as file202:
         wrt=csv.writer(file202)
         wrt.writerow(['Name','Quantity','Price(rs)'])
sname=' '
#to set shop name
def setname():
    ssname=input("enter shop name:")
    print(f"shop name has been set to {sname}")
    with open('sname.txt','w') as namee:
        namee.write(ssname)
    print(f"\nsuccesfully set shop name as {ssname}")

#to input items into the csv file
def inputitem():
    global code
    ap=open("items.csv","a",newline='')
    w=csv.writer(ap)
    a,n='',0
    while a.lower()!="done":
        a=input("Item name(type done to stop):").strip()
        if a!="done":
            qty=int(input("enter quantity:"))
            price=int(input('enter price:'))
            w.writerow([a.lower(),qty,price])
            n+=1
    print(f"\nSuccessfully added {n} items to items.csv")

#to print the items csv
def show():
    table = PrettyTable()
    with open('items.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        table.field_names = headers
        for row in reader:
            table.add_row(row)
    print(table)
    
#billing function
def bill():
    global sname
    with open('sname.txt','r') as reaad:
        sss=reaad.read()
        sname=str(sss)
    billamnt=0
    user=input("customer name:")
    n=int(input("mobile number:"))
    table = PrettyTable()
    table.field_names = ["Name", "Quantity", "Price"]
    a=''
    data = pd.read_csv("items.csv")
    while a!='done':
        a=input('enter item name(type done to stop):').lower().strip()
        if a!="done":
            qty=int(input('enter quantity:'))
            with open('items.csv', 'r') as file1:
                reader1 = csv.DictReader(file1)
                for row in reader1:
                    if row['Name'] == a:
                        qty1=(int(row['Quantity']))
            if (qty1-qty)<0:
                print(f"only {qty1} {a} are left")
            else:
                data.loc[data["Name"]==a, "Quantity"] = (qty1-qty)
                data.to_csv("items.csv", index=False)
                with open('items.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['Name'] == a:
                            pric=(int(row['Price(rs)']))
                billamnt+=pric*(int((qty**2)**0.5))
                table.add_row([a, qty, str(pric*qty)+f"\u20B9"])
    billp=f'\n\n**************************************************************\n                    |{sname}|\n  >name:{user}\n  >contactno:{n}\n  >date:{date.today()}\n**************************************************************\n\n{table}\n                 grand total:{str(billamnt)+"₹"}\n\n Thank You for purchasing from us\n**************************************************************'
    print(billp)
    with open(f'bill_{n}.txt','w',encoding="utf-8") as billt:
        billt.write(billp)
        billt.close()
        print(f"bill is saved in your system as bill_{n}.txt")

#add stock
def addstock():
    a=input("enter item name to add quantity: ").lower().strip()
    n=int(input("enter quantity to be added: "))
    data = pd.read_csv("items.csv")
    with open('items.csv', 'r') as file1:
                reader1 = csv.DictReader(file1)
                for row in reader1:
                    if row['Name'] == a:
                        qty=(int(row['Quantity']))
    data.loc[data["Name"]==a, "Quantity"] = (qty+n)
    data.to_csv("items.csv", index=False)
    print(f"\nsuccesfully added {n} more {a} to the quantity")

#delete item
def delete():
    a=input("enter item name to be deleted: ").lower().strip()
    df=pd.read_csv("items.csv",index_col="Name")
    df=df.drop(a)
    df.to_csv("items.csv",index=True)
    print(f"\nsuccesfully deleted {a} from items.csv")

#user define
ch='Y'
print('Hi This is Python store management system\n')
while ch.upper().strip()=='Y':
    print('>>>we have 6 main commands:')
    print('setname     -     >Allows Shop owner to set their shop \n                    name to be shown in the bill\n')
    print('input       -     >Enables Shop owner to input\n                    item name, quantity, price\n                    in a csv file\n')
    print('add         -     >Enebles Shop owner to add more\n                  quantity to an item\n')
    print('delete      -     >Allows Shop owner to delete a\n                   specific item\n')
    print('show        -     >Displays the csv file of items\n')
    print('bill        -     >Lets the Cashier/owner create\n                    a bill for customer which will\n                    be displayed and saved in the\n                    system as txt file\n')
    print("\n**************************************************************\n**************************************************************\n")
    choice=input("enter command to be done: ")
    if choice.lower().strip()=="setname": setname()
    if choice.lower().strip()=="input": inputitem()
    if choice.lower().strip()=="show": show()
    if choice.lower().strip()=="bill": bill()
    if choice.lower().strip()=="add": addstock()
    if choice.lower().strip()=="delete": delete()
    print("\n**************************************************************\n**************************************************************\n")
    ch=input("do u want to execute another command?(Y/N): ")

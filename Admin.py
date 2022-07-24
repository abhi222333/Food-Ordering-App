import random

admin_Information = {"Abhishek": "Abhi280522"}

All_Item = {1: {'ItemName': 'Tandoori Momos', 'ItemID': 1, 'Price': 180, 'Quantity': 12 , 'Stock': 24, 'Discount': 10},
        2: {'ItemName': 'Paneer Burger', 'ItemID': 2, 'Quantity': 1, 'Price': 80, 'Stock': 20, 'Discount': 5},
        10: {'ItemName': 'Coke', 'ItemID': 10, 'Quantity': 1 , 'Price': 80, 'Stock': 0, 'Discount': 5},
        15: {'ItemName': 'Black Forest Cake', 'ItemID': 15, 'Quantity': 1, 'Price': 450, 'Stock': 10, 'Discount': 20}}

def add_new_item():
     for i in All_Item:
        itemid = random.randint(0,100)
        if  All_Item[i]["ItemID"] != itemid:
            itemname = input("Enter the Item name: ")    
            price = int(input("Enter the price of the item: "))
            quantity= int(input("Enter the quantity of the item: "))
            stock = int(input("Enter the stock value of item: "))
            discount = int(input("Enter the discount value of item: "))
            All_Item[itemid] = {
                 "ItemName": itemname,
                 "ItemID": itemid,
                 "Price": price,
                 "Quantity":quantity,
                 "Stock": stock,
                 "Discount": discount
                }
            print("The Item "+ itemname + " is successfully added")
            return All_Item


def edit_food_item():
     view_list()
     item = int(input("Enter the itemid which you want to edit: "))
     a = input("Enter the item name : ")
     b = int(input("Enter the price of item : "))
     d = int(input("Enter the stock of the item : "))
     All_Item[item]["ItemName"] = a
     All_Item[item]["Price"] = b
     All_Item[item]["Stock"] = d
     print("*Edited item successfully*") 
     return All_Item

def show_stock():
     
    print("*HERE IS THE All THE STOCK OF FoodApp*",'\n')
    for i in All_Item:
        if  All_Item[i]["Stock"] > 0:
            print("Item ID: ",All_Item[i]["ItemID"])
            print("Item Name: ",All_Item[i]["ItemName"])
            print("Price: ",All_Item[i]["Price"],"INR")
            print("Quantity: ",All_Item[i]["Quantity"],"Piece")
            print("Stock: ",All_Item[i]["Stock"],'\n')
    
def view_list():
     
    print("*HERE IS THE All Item of FoodApp*",'\n')
    for i in All_Item:
        print("Item ID: ",All_Item[i]["ItemID"])
        print("Item Name: ",All_Item[i]["ItemName"])
        print("Price: ",All_Item[i]["Price"],"INR")
        print("Quantity: ",All_Item[i]["Quantity"],"Piece \n")
    
       
def remove_item():
    d = int(input(" Enter the Item id of Food which you want to Remove Permanently from your Database: "))
    All_Item.pop(d)
    print("Remove item successfully ")
    return All_Item

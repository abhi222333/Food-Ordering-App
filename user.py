import Admin as ad
import random

class User:
    User_Profile={212: {"User ID": 212, "Phone No.":123456780,"User Name":'Yash', "Address": 'Greater Noida' ,"Email": 'Yash123@Edyoda.com', "Password":'Yash@123' }}
    login_info = {'Yash' : 'Yash@123' }
    order_history = {}

    def _init_(self, userid, name, phoneno, email, address, password):
        self.userid = userid
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.name] = self.password
        self.profile={"User Name":name}

    def user_signup(self):
        for i in User.User_Profile:
            userid = random.randint(100,999)
            if  User.User_Profile[i]["User ID"] != userid:
                phoneno = int(input("Enter the Phone Number: "))
                name =input("Enter the user name: ")
                address = input("Enter the Address of User : ")
                email =input("Enter Email ID of User : ")
                password = input("Enter the Password: ")
                User.User_Profile[userid] ={
                    "User ID" : userid,
                    "Phone No.": phoneno,
                    "User Name": name,
                    "Address": address,
                    "Email": email,
                    "Password":password
                    }
                r = { name : password }
                User.login_info.update(r)
                print(f"The user {name} with User ID {userid} is successfully registered",'\n')
               
                return User.User_Profile

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("*****You're are successfully logged in*****")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False

    def update_profile(self):
        ID = int(input("Enter the User ID which you want to edit: "))
        a = input("Enter the item User Name : ")
        b = int(input("Enter the User Phone Number : "))
        c = input("Enter the User Address : ")
        d = input("Enter the User Email ID : ")
        e = input("Enter new Password : ")
        User.User_Profile[ID]["User Name"] = a
        User.User_Profile[ID]["Phone No."] = b
        User.User_Profile[ID]["Address"] = c
        User.User_Profile[ID]["Email"] = d
        User.User_Profile[ID]["Password"] = e

        User.login_info= { a : e }
        
        print("**Profile Updated successfully*") 
        return User.User_Profile
    


    def place_order(self):
        print("What you want to order here in the Inventory")
        print(ad.show_stock())
        user_choice = int(input("If you want to order then select 1.YES 2.NO \n"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order : "))
            x=0
            for i in range(n):
             
             itemid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             x += (ad.All_Item[itemid]["Price"] * quan/(ad.All_Item[itemid]["Quantity"])-(ad.All_Item[itemid]["Discount"]))
             self.order_history[itemid] = {
                    "Item Name": ad.All_Item[itemid]["ItemName"],
                    "Price": ad.All_Item[itemid]["Price"],
                    "Quantity": quan
                }
            print(f"It costs you {x}INR in total")
            print("You're all set for this order")
            
            again_ask = input("Are you want to order this Enter YES or NO \n")
            if again_ask == "YES":
                
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

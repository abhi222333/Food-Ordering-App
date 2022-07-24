import Admin as AA
from user import User

u = User()


First_Look_crawler = True
while First_Look_crawler :    
    First_Look = int(input("Welcome to FoodApp Select 1.SignUp 2. login and 3.Exit \n"))
    if First_Look == 1:
        sign_up_crawler = True
        while sign_up_crawler:
            user_input = int(input(" Welcom to FoodApp user Sign up Pannel 1. SignUp 2. Exit the Pannel \n"))
            if user_input == 1:
                print(" Enter all details to be for signUp as User ",'\n')
                u.user_signup()            
            else:
                sign_up_crawler = False
    elif First_Look == 2:
        inp = int(input("Where do you want to login Select 1.Admin and 2.User and 3.Exit \n"))
        if inp == 1:
            Username = input("Enter the username of admin: ")
            Password = input("Enter the password of admin: ")
            if AA.admin_Information[Username] == Password:
                print(" You are successfully logged to FoodApp ",'\n')
                admin_crawler = True
                while admin_crawler:
                    admin_options = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW STOCK 4.REMOVE ITEM 5.VIEW LIST OF ALL ITEM 6.EXIT \n"))
                    if admin_options == 1:
                        AA.add_new_item()
                    elif admin_options == 2:
                        AA.edit_food_item()
                    elif admin_options == 3:
                        AA.show_stock()
                    elif admin_options == 4:
                        AA.remove_item()
                    elif admin_options == 5:
                        AA.view_list()
                    elif admin_options == 6:
                        print(f"You're Exit to the admin panel {Username}",'\n')
                        admin_crawler = False
                    else:
                        print("This is the wrong selection please select valid option",'\n')
            else:
                print("These are the wrong credentials! SORRY!!!")
        elif inp == 2:
            print("Welcome to the user panel",'\n')
            username = input("Enter the username here: ")
            password = input("Enter the password here: ")
            if User.login(username, password):
                print(f"You are logged in successfully {username}",'\n')
                user_crawler = True
                while user_crawler:
                    usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Update Profile 3.Order history 4.Exit \n"))
                    if usr_choice == 1:
                        u.place_order()
                    elif usr_choice == 2:
                        print("Enter Details to Update Profile")
                        u.update_profile()
                    elif usr_choice == 3:
                        print(f"Here is your order history, {username}",'\n')
                        print(u.order_history)
                    elif usr_choice == 4:
                        user_crawler = False
                        print("You're Successfully looged out",'\n')
                    else:
                        print("You choose the invalid option")
            else:
                print("These are the wrong credentials! SORRY!!! TRY AGAIN",'\n')
        else:
            exit()
    else:
        First_Look_crawler = True
        exit()
else:
    exit()

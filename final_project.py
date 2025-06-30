#Sanjana Sridhar
#Created on 01/04/25

account_info = {"san": {"name": "Sanjana Sridhar", "balance": 0.0, "password": "1234"} }  # stores User ID as key and a dictionary with name, balance, and password as value

# defining the functions
def load_acc(file_path):
    #checks if accounts exist in file
    file = open(file_path, "r")
    for line in file:
        line = line.strip()
        if not line or line.count(",") != 3:  # Ensure the line has exactly 3 commas
            continue  # Skip invalid or empty lines
        user_id, name, balance, password = line.split(",")
        account_info[user_id] = {"name": name, "balance": float(balance), "password": password}

def save_acc(file_path):
    #adds new accounts to file
    file = open(file_path, "w")
    for user_id in account_info:
        data = account_info[user_id]  #accesses the value using the user_id
        file.write(f"{user_id},{data['name']},{data['balance']:.2f},{data['password']}\n")
    file.close()

def login_screen():
    login_choice = int(input('''Welcome to PyBank
--------------------------
--------------------------
Press 1 to LOG IN...
Press 2 to CREATE NEW ACCOUNT: '''))
    return login_choice

def deposit(user_id, deposit_amount):
    print("2.0% interest! Good for you!") 
    account_info[user_id]["balance"] += float(1.02 * deposit_amount) #calculating interest
    return account_info[user_id]["balance"]

def withdrawal(user_id, withdrawal_amount):
    if withdrawal_amount > account_info[user_id]["balance"]:
        print("Not enough funds in balance.")
    else:
        account_info[user_id]["balance"] -= float(withdrawal_amount)
    return account_info[user_id]["balance"]

def user_exist(user_id):
    if user_id in account_info:
        return True  #if the user ID already exists
    return False
    
def create_account():
    customer_name = input("Enter your name: ")
    user_id = input("Enter a NEW User ID: ")
    password = input("Enter a NEW Password: ")
    if user_exist(user_id):  #if account already exists
        print("User ID already exists.")
        return None
    initial_balance = 0.0
    account_info[user_id] = {"name": customer_name, "balance": initial_balance, "password": password}
    print(f"Account successfully created.")
    return user_id

def log_in():
    user_id = input("Enter your User ID: ")
    password = input("Enter your Password: ")
    if not user_exist(user_id):  #if account doesn't exist
        print("User ID does not exist.")
        return None
    if account_info[user_id]["password"] != password: #if password is incorrect
        print("Incorrect Password.")
        return None
    print("Login successful!")
    return user_id

def account(user_id):  # displaying account information
    customer_name = account_info[user_id]["name"]
    balance = account_info[user_id]["balance"]
    print(f"Customer Name: {customer_name}")
    print(f"Balance: ${balance:.2f}")

def acc_options():
    press_num = int(input('''Press 1 to make a deposit
Press 2 to make a withdrawal
Press 9 to Quit: '''))
    return press_num

file_path = "PyBank_app.txt"
load_acc(file_path)

# main program loop
while True:
    print(" ")  # organization :)
    choice = login_screen()
    print(" ")
    if choice == 1:  # LOG IN
        user_id = log_in()
        if user_id is None:  # if login failed
            continue
        print(" ")
        account(user_id)
        print(" ")
        # transaction loop for logged-in user
        while True:
            press_num = acc_options()
            print(" ")
            if press_num == 1:  # deposit
                deposit_amount = float(input("Enter the deposit amount: "))
                new_balance = deposit(user_id, deposit_amount)
                account(user_id)
                save_acc(file_path)
                print(" ")
            elif press_num == 2:  # withdrawal
                withdrawal_amount = float(input("Enter the withdrawal amount: "))
                new_balance = withdrawal(user_id, withdrawal_amount)
                account(user_id)
                save_acc(file_path)
                print(" ")
            elif press_num == 9:  # log out
                print("Logging out...")
                print(" ")
                save_acc(file_path)
                break
            else:
                print("Invalid Input")
    elif choice == 2:  # CREATE NEW ACCOUNT
        user_id = create_account()
        save_acc(file_path)
    else:
        print("Invalid choice.")

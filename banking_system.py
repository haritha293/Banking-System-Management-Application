import MySQLdb as mysql

# MySQL connection parameters
host_name = "localhost"
user_name = "your_username"
password = "your_password"
database_name = "banking_system"

# Establish a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connect(
            host="localhost",
            user="root",
            password="Root",
            database="banking_system"
        )
        return connection
    except Exception as e:
        print(f"Error: '{e}'")

# Create a new account
def create_account(name, email, balance):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO accounts (name, email, balance) VALUES (%s, %s, %s)"
        val = (name, email, balance)
        cursor.execute(sql, val)
        connection.commit()
        print("Account created successfully!")
        connection.close()
    else:
        print("Failed to create account.")

# Deposit money into an account
def deposit_money(account_number, amount):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
        val = (amount, account_number)
        cursor.execute(sql, val)
        connection.commit()
        print("Deposit successful!")
        connection.close()
    else:
        print("Failed to deposit money.")

# Withdraw money from an account
def withdraw_money(account_number, amount):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT balance FROM accounts WHERE account_number = %s"
        val = (account_number,)
        cursor.execute(sql, val)
        balance = cursor.fetchone()[0]
        if balance >= amount:
            sql = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
            val = (amount, account_number)
            cursor.execute(sql, val)
            connection.commit()
            print("Withdrawal successful!")
        else:
            print("Insufficient balance.")
        connection.close()
    else:
        print("Failed to withdraw money.")

# Display account information
def display_account_info(account_number):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM accounts WHERE account_number = %s"
        val = (account_number,)
        cursor.execute(sql, val)
        account_info = cursor.fetchone()
        if account_info:
            print("Account Number:", account_info[0])
            print("Name:", account_info[1])
            print("Email:", account_info[2])
            print("Balance:", account_info[3])
        else:
            print("Account not found.")
        connection.close()
    else:
        print("Failed to display account information.")

# Main program
def main():
    while True:
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Information")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            balance = float(input("Enter your initial balance: "))
            create_account(name, email, balance)
        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to deposit: "))
            deposit_money(account_number, amount)
        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter the amount to withdraw: "))
            withdraw_money(account_number, amount)
        elif choice == "4":
            account_number = int(input("Enter your account number: "))
            display_account_info(account_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
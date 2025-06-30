# PyBank App

A simple Python banking application that allows users to create accounts, log in, and manage their balances. Data is stored in a text file to simulate persistent account management.

## Features

- **Login or Create Account**
  - Users can log in with an existing User ID and password or create a new account with a unique User ID.

- **Account Storage**
  - All user data is saved in `PyBank_app.txt`.
  - Each line follows this format:
    ```
    UserID, Customer Name, Account Balance, Password
    ```

- **Banking Options**
  - Deposit money (automatically adds 2% interest).
  - Withdraw money (only if the balance is sufficient).
  - Balance updates are immediate and saved to the file.

- **Logout System**
  - Press `9` to log out and return to the login screen.

## What I Learned

- Reading and writing to files in Python
- Basic user authentication
- Using loops and conditionals to control program flow
- Implementing simple interest logic
- Creating a multi-step menu system

## Future Improvements

- Encrypt stored passwords for security
- Add a transaction history feature
- Build a graphical version using Tkinter

## Flowchart

![App Flowchart](images/flowchart.png)

class ATM:
    def __init__(self):
        self.pin = None
        self.balance = 0.0

    def create_pin(self):
        if self.pin is None:
            self.pin = input("Set your new 4-digit PIN: ")
            print("PIN created successfully.")
        else:
            print("PIN is already set. Use option 2 to change it.")

    def change_pin(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            self.pin = input("Enter new PIN: ")
            print("PIN changed successfully.")
        else:
            print("Incorrect current PIN.")

    def deposit(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return
        entered_pin = input("Enter PIN: ")
        if entered_pin == self.pin:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. Current Balance: ₹{self.balance:.2f}")
        else:
            print("Incorrect PIN.")

    def withdraw(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return
        entered_pin = input("Enter PIN: ")
        if entered_pin == self.pin:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. Remaining Balance: ₹{self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")

    def check_balance(self):
        if self.pin is None:
            print("Please create a PIN first.")
            return
        entered_pin = input("Enter PIN: ")
        if entered_pin == self.pin:
            print(f"Your current balance is: ₹{self.balance:.2f}")
        else:
            print("Incorrect PIN.")


atm = ATM()

while atm.pin is None:
    print("\nPlease create a PIN before using ATM services.")
    atm.create_pin()

while True:
    print("\n=== ATM Menu ===")
    print("1. Change PIN")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        atm.change_pin()
    elif choice == '2':
        atm.deposit()
    elif choice == '3':
        atm.withdraw()
    elif choice == '4':
        atm.check_balance()
    elif choice == '5':
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Try again.")
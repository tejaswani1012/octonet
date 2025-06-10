import datetime

class ATM:
    def __init__(self):
        self.balance = 10000  # Initial balance
        self.pin = "1234"     # Default PIN
        self.transaction_history = []

    def log_transaction(self, action, amount=0):
        now = datetime.datetime.now()
        entry = f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {action}: ₹{amount}" if amount else f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {action}"
        self.transaction_history.append(entry)

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("Access granted.\n")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. Attempts left: {attempts}")
        print("Account locked due to too many incorrect attempts.")
        return False

    def show_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")
        self.log_transaction("Balance Inquiry")

    def withdraw_cash(self):
        try:
            amount = int(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Invalid amount.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"Please collect your cash: ₹{amount}")
                self.log_transaction("Withdrawal", amount)
        except ValueError:
            print("Invalid input.")

    def deposit_cash(self):
        try:
            amount = int(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("Invalid amount.")
            else:
                self.balance += amount
                print(f"₹{amount} has been deposited to your account.")
                self.log_transaction("Deposit", amount)
        except ValueError:
            print("Invalid input.")

    def change_pin(self):
        old_pin = input("Enter current PIN: ")
        if old_pin != self.pin:
            print("Incorrect current PIN.")
            return
        new_pin = input("Enter new 4-digit PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            print("PIN successfully changed.")
            self.log_transaction("PIN Change")
        else:
            print("PIN change failed. Ensure the new PIN is 4 digits and both entries match.")

    def view_transaction_history(self):
        print("\n--- Transaction History ---")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for entry in self.transaction_history:
                print(entry)

def main():
    atm = ATM()
    if not atm.authenticate():
        return

    while True:
        atm.show_menu()
        choice = input("Select an option (1-6): ")
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            atm.withdraw_cash()
        elif choice == "3":
            atm.deposit_cash()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.view_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
import tkinter as tk  
from tkinter import messagebox, simpledialog  

class ATM:  
    def __init__(self, master):  
        self.master = master  
        self.master.title("ATM")  
        self.master.geometry("400x400")  
        self.master.configure(bg="#F0F8FF")  # Light Alice Blue background  

        self.pin = "1234"  # Sample PIN  
        self.balance = 0.0  # Initial balance  
        self.transactions = []  

        # PIN Entry  
        self.pin_label = tk.Label(self.master, text="Enter your PIN:", font=("Helvetica", 18), bg="#F0F8FF", fg="#005f73")  
        self.pin_label.pack(pady=20)  

        self.pin_entry = tk.Entry(self.master, show="*", font=("Helvetica", 18))  
        self.pin_entry.pack(pady=10)  

        self.login_button = tk.Button(self.master, text="Login", command=self.verify_pin, bg="#008CBA", fg="#FFFFFF", font=("Helvetica", 16), width=15)  
        self.login_button.pack(pady=20)  

    def verify_pin(self):  
        entered_pin = self.pin_entry.get()  
        if entered_pin == self.pin:  
            self.pin_label.pack_forget()  
            self.pin_entry.pack_forget()  
            self.login_button.pack_forget()  
            self.show_menu()  
        else:  
            messagebox.showwarning("Login Failed", "Incorrect PIN. Please try again.")  

    def show_menu(self):  
        menu_title = tk.Label(self.master, text="Main Menu", font=("Helvetica", 24), bg="#F0F8FF", fg="#005f73")  
        menu_title.pack(pady=20)  

        self.balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance, bg="#00BFFF", fg="#FFFFFF", font=("Helvetica", 16), width=20)  
        self.balance_button.pack(pady=10)  

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit_cash, bg="#32CD32", fg="#FFFFFF", font=("Helvetica", 16), width=20)  
        self.deposit_button.pack(pady=10)  

        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw_cash, bg="#FF4500", fg="#FFFFFF", font=("Helvetica", 16), width=20)  
        self.withdraw_button.pack(pady=10)  

        self.change_pin_button = tk.Button(self.master, text="Change PIN", command=self.change_pin, bg="#FFD700", fg="#000000", font=("Helvetica", 16), width=20)  
        self.change_pin_button.pack(pady=10)  

        self.history_button = tk.Button(self.master, text="Transaction History", command=self.get_transaction_history, bg="#8A2BE2", fg="#FFFFFF", font=("Helvetica", 16), width=20)  
        self.history_button.pack(pady=10)  

    def check_balance(self):  
        messagebox.showinfo("Balance", f"Your balance is: ${self.balance:.2f}")  

    def deposit_cash(self):  
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")  
        if amount is None:  
            return  
        if amount > 0:  
            self.balance += amount  
            self.transactions.append(f"Deposited: ${amount:.2f}")  
            messagebox.showinfo("Deposit", f"Successfully deposited ${amount:.2f}.")  
        else:  
            messagebox.showwarning("Deposit", "Deposit amount must be positive.")  

    def withdraw_cash(self):  
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")  
        if amount is None:  
            return  
        if 0 < amount <= self.balance:  
            self.balance -= amount  
            self.transactions.append(f"Withdrew: ${amount:.2f}")  
            messagebox.showinfo("Withdraw", f"Successfully withdrew ${amount:.2f}.")  
        else:  
            messagebox.showwarning("Withdraw", "Insufficient balance or invalid amount.")  

    def change_pin(self):  
        old_pin = simpledialog.askstring("Change PIN", "Enter your old PIN:")  
        if old_pin == self.pin:  
            new_pin = simpledialog.askstring("Change PIN", "Enter your new PIN:")  
            if new_pin and len(new_pin) == 4:  
                self.pin = new_pin  
                messagebox.showinfo("Change PIN", "PIN changed successfully.")  
            else:  
                messagebox.showwarning("Change PIN", "New PIN must be 4 digits.")  
        else:  
            messagebox.showwarning("Change PIN", "Incorrect old PIN.")  

    def get_transaction_history(self):  
        if self.transactions:  
            history = "\n".join(self.transactions)  
            messagebox.showinfo("Transaction History", history)  
        else:  
            messagebox.showinfo("Transaction History", "No transactions yet.")  

def main():  
    root = tk.Tk()  
    app = ATM(root)  
    root.mainloop()  

if __name__ == "__main__":  
    main()




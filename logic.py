from PySide6.QtWidgets import QMainWindow
from csv import DictReader
from window import Ui_MainWindow

class mainWindow(Ui_MainWindow):
    def __init__(self):
        # Init the window using the Ui_MainWindow class inherited from window.py
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        # Read the accounts from the accounts.csv file and store them in a list of dictionaries
        with open("accounts.csv", 'r') as file:
            lines = DictReader(file)
            self.accounts = list(lines)
            # Dummy value so later functions don't crash before login
            self.current_account = 0

        # Set up button connections
        self.setupButtons()

    def setupButtons(self):
        # Connect the buttons to their respective functions
        # Login menu buttons
        self.ui.pushButton_zero.clicked.connect(lambda: self.addText("0"))
        self.ui.pushButton_one.clicked.connect(lambda: self.addText("1"))
        self.ui.pushButton_two.clicked.connect(lambda: self.addText("2"))
        self.ui.pushButton_three.clicked.connect(lambda: self.addText("3"))
        self.ui.pushButton_four.clicked.connect(lambda: self.addText("4"))
        self.ui.pushButton_five.clicked.connect(lambda: self.addText("5"))
        self.ui.pushButton_six.clicked.connect(lambda: self.addText("6"))
        self.ui.pushButton_seven.clicked.connect(lambda: self.addText("7"))
        self.ui.pushButton_eight.clicked.connect(lambda: self.addText("8"))
        self.ui.pushButton_nine.clicked.connect(lambda: self.addText("9"))
        self.ui.pushButton_backspace.clicked.connect(lambda: self.subText())
        self.ui.pushButton_confirm.clicked.connect(lambda: self.confirm())
        # Main menu buttons
        self.ui.pushButton_L1.clicked.connect(lambda: self.gotoWithdraw())
        self.ui.pushButton_L2.clicked.connect(lambda: self.gotoTransfer())
        self.ui.pushButton_L4.clicked.connect(lambda: self.gotoLogin())
        self.ui.pushButton_R1.clicked.connect(lambda: self.gotoDeposit())
        self.ui.pushButton_R2.clicked.connect(lambda: self.gotoBalance())
        self.ui.pushButton_R4.clicked.connect(lambda: self.gotoAccount())
        # Withdraw menu buttons
        self.ui.pushButton_zero_w.clicked.connect(lambda: self.addText_w("0"))
        self.ui.pushButton_one_w.clicked.connect(lambda: self.addText_w("1"))
        self.ui.pushButton_two_w.clicked.connect(lambda: self.addText_w("2"))
        self.ui.pushButton_three_w.clicked.connect(lambda: self.addText_w("3"))
        self.ui.pushButton_four_w.clicked.connect(lambda: self.addText_w("4"))
        self.ui.pushButton_five_w.clicked.connect(lambda: self.addText_w("5"))
        self.ui.pushButton_six_w.clicked.connect(lambda: self.addText_w("6"))
        self.ui.pushButton_seven_w.clicked.connect(lambda: self.addText_w("7"))
        self.ui.pushButton_eight_w.clicked.connect(lambda: self.addText_w("8"))
        self.ui.pushButton_nine_w.clicked.connect(lambda: self.addText_w("9"))
        self.ui.pushButton_backspace_w.clicked.connect(lambda: self.subText_w())
        self.ui.pushButton_point_w.clicked.connect(lambda: self.addText_w("."))
        self.ui.pushButton_L1_w.clicked.connect(lambda: self.withdraw(20))
        self.ui.pushButton_L2_w.clicked.connect(lambda: self.withdraw(40))
        self.ui.pushButton_L3_w.clicked.connect(lambda: self.withdraw(60))
        self.ui.pushButton_L4_w.clicked.connect(lambda: self.gotoMain())
        self.ui.pushButton_R1_w.clicked.connect(lambda: self.withdraw(80))
        self.ui.pushButton_R2_w.clicked.connect(lambda: self.withdraw(100))
        self.ui.pushButton_R3_w.clicked.connect(lambda: self.withdraw(120))
        self.ui.pushButton_R4_w.clicked.connect(lambda: self.withdraw(self.ui.inputLine_w.text()))
        # Deposit menu buttons
        self.ui.pushButton_zero_d.clicked.connect(lambda: self.addText_d("0"))
        self.ui.pushButton_one_d.clicked.connect(lambda: self.addText_d("1"))
        self.ui.pushButton_two_d.clicked.connect(lambda: self.addText_d("2"))
        self.ui.pushButton_three_d.clicked.connect(lambda: self.addText_d("3"))
        self.ui.pushButton_four_d.clicked.connect(lambda: self.addText_d("4"))
        self.ui.pushButton_five_d.clicked.connect(lambda: self.addText_d("5"))
        self.ui.pushButton_six_d.clicked.connect(lambda: self.addText_d("6"))
        self.ui.pushButton_seven_d.clicked.connect(lambda: self.addText_d("7"))
        self.ui.pushButton_eight_d.clicked.connect(lambda: self.addText_d("8"))
        self.ui.pushButton_nine_d.clicked.connect(lambda: self.addText_d("9"))
        self.ui.pushButton_backspace_d.clicked.connect(lambda: self.subText_d())
        self.ui.pushButton_point_d.clicked.connect(lambda: self.addText_d("."))
        self.ui.pushButton_L1_d.clicked.connect(lambda: self.deposit(20))
        self.ui.pushButton_L2_d.clicked.connect(lambda: self.deposit(40))
        self.ui.pushButton_L3_d.clicked.connect(lambda: self.deposit(60))
        self.ui.pushButton_L4_d.clicked.connect(lambda: self.gotoMain())
        self.ui.pushButton_R1_d.clicked.connect(lambda: self.deposit(80))
        self.ui.pushButton_R2_d.clicked.connect(lambda: self.deposit(100))
        self.ui.pushButton_R3_d.clicked.connect(lambda: self.deposit(120))
        self.ui.pushButton_R4_d.clicked.connect(lambda: self.deposit(self.ui.inputLine_d.text()))
        # Transfer menu buttons
        self.ui.pushButton_zero_t.clicked.connect(lambda: self.addText_t("0"))
        self.ui.pushButton_one_t.clicked.connect(lambda: self.addText_t("1"))
        self.ui.pushButton_two_t.clicked.connect(lambda: self.addText_t("2"))
        self.ui.pushButton_three_t.clicked.connect(lambda: self.addText_t("3"))
        self.ui.pushButton_four_t.clicked.connect(lambda: self.addText_t("4"))
        self.ui.pushButton_five_t.clicked.connect(lambda: self.addText_t("5"))
        self.ui.pushButton_six_t.clicked.connect(lambda: self.addText_t("6"))
        self.ui.pushButton_seven_t.clicked.connect(lambda: self.addText_t("7"))
        self.ui.pushButton_eight_t.clicked.connect(lambda: self.addText_t("8"))
        self.ui.pushButton_nine_t.clicked.connect(lambda: self.addText_t("9"))
        self.ui.pushButton_backspace_t.clicked.connect(lambda: self.subText_t)
        self.ui.pushButton_point_t.clicked.connect(lambda: self.addText_t("."))
        self.ui.pushButton_L1_t.clicked.connect(lambda: self.transfer(20, self.ui.acctnumLine_t.text()))
        self.ui.pushButton_L2_t.clicked.connect(lambda: self.transfer(40, self.ui.acctnumLine_t.text()))
        self.ui.pushButton_L3_t.clicked.connect(lambda: self.transfer(60, self.ui.acctnumLine_t.text()))
        self.ui.pushButton_L4_t.clicked.connect(lambda: self.gotoMain())
        self.ui.pushButton_R1_t.clicked.connect(lambda: self.transfer(80, self.ui.acctnumLine_t.text()))
        self.ui.pushButton_R2_t.clicked.connect(lambda: self.transfer(100, self.ui.acctnumLine_t.text()))
        self.ui.pushButton_R3_t.clicked.connect(lambda: self.transfer(120, self.ui.acctnumLine_t.text()))
        self.ui.pushButton_R4_t.clicked.connect(lambda: self.transfer(self.ui.inputLine_t.text(), self.ui.acctnumLine_t.text()))
        # Balance menu buttons
        self.ui.pushButton_L4_b.clicked.connect(lambda: self.gotoMain())
        # Account menu buttons
        self.ui.pushButton_L4_a.clicked.connect(lambda: self.gotoMain())

    # Login menu function(s)
    def addText(self, text):
        # Add text to the line edit field
        current_text = str(self.ui.inputLine.text())
        new_text = current_text + text
        self.ui.inputLine.setText(new_text)
    def subText(self):
        # Delete one character from the text in the line edit field
        current_text = str(self.ui.inputLine.text())
        new_text = current_text[:-1]
        self.ui.inputLine.setText(new_text)
    def confirm(self):
        # See if input matched any of the accounts in the accounts.csv file
        input_text = str(self.ui.inputLine.text())
        account_found = False
        for index, account in enumerate(self.accounts):
            if input_text == str(account["Pin"]):
                self.ui.inputLine.setText("")
                self.ui.errorLabel.setText("")
                account_found = True
                self.current_account = index
                self.gotoMain()
        if not account_found:
            self.ui.inputLine.setText("")
            self.ui.errorLabel.setText("Invalid Pin. Try again.")

    # Withdraw menu function(s)
    def addText_w(self, text):
        # Add text to the line edit field
        current_text = self.ui.inputLine_w.text()
        new_text = current_text + text
        self.ui.inputLine_w.setText(new_text)
    def subText_w(self):
        # Delete one character from the text in the line edit field
        current_text = self.ui.inputLine_w.text()
        new_text = current_text[:-1]
        self.ui.inputLine_w.setText(new_text)
    def withdraw(self, num):
        # Test input for validity
        try:
            num = float(num)
        except:
            self.ui.label_top_w.setText("Invalid input.")
            return
        # Withdraw the specified amount from the current account
        balance = float(self.accounts[self.current_account]["Balance"])
        if balance >= num:
            balance -= num
            self.accounts[self.current_account]["Balance"] = balance
            self.ui.label_top_w.setText(f"Withdrew ${num:.2f}.")
            self.ui.label_bottom_w.setText(f"Balance: ${balance:.2f}")
            self.updateAccounts()
        else:
            self.ui.label_top_w.setText("Insufficient funds.")
    
    # Deposit menu function(s)
    def addText_d(self, text):
        # Add text to the line edit field
        current_text = self.ui.inputLine_d.text()
        new_text = current_text + text
        self.ui.inputLine_d.setText(new_text)
    def subText_d(self):
        # Delete one character from the text in the line edit field
        current_text = self.ui.inputLine_d.text()
        new_text = current_text[:-1]
        self.ui.inputLine_d.setText(new_text)
    def deposit(self, num):
        # Test input for validity
        try:
            num = float(num)
        except:
            self.ui.label_top_d.setText("Invalid input.")
            return
        # Deposit the specified amount to the current account
        balance = float(self.accounts[self.current_account]["Balance"])
        balance += num
        self.accounts[self.current_account]["Balance"] = balance
        self.ui.label_top_d.setText(f"Deposited ${num:.2f}.")
        self.ui.label_bottom_d.setText(f"Balance: ${balance:.2f}")
        self.updateAccounts()

    # Transfer menu function(s)
    def addText_t(self, text):
        # Add text to the line edit field
        current_text = self.ui.inputLine_t.text()
        new_text = current_text + text
        self.ui.inputLine_t.setText(new_text)
    def subText_t(self):
        # Delete one character from the text in the line edit field
        current_text = self.ui.inputLine_t.text()
        new_text = current_text[:-1]
        self.ui.inputLine_t.setText(new_text)
    def transfer(self, num, acctnum):
        # Test input for validity
        try:
            num = float(num)
        except:
            self.ui.label_top_t.setText("Invalid input.")
            return
        # Find the account to transfer to (input does not need to be validated because the field is masked to only accept numbers)
        acct_found = False
        for index, account in enumerate(self.accounts):
            if acctnum == account["Pin"]:
                acct_found = True
                transfer_account = index
        if not acct_found:
            self.ui.label_top_t.setText("Account not found.")
            return
        # Transfer the specified amount from the current account to the transfer account
        balance = float(self.accounts[self.current_account]["Balance"])
        if balance >= num:
            balance -= num
            self.accounts[self.current_account]["Balance"] = balance
            transfer_balance = float(self.accounts[transfer_account]["Balance"])
            transfer_balance += num
            self.accounts[transfer_account]["Balance"] = f"{transfer_balance:.2f}"
            self.ui.label_top_t.setText(f"Transferred ${num:.2f} to {self.accounts[transfer_account]['Name']}.")
            self.ui.label_bottom_t.setText(f"Balance: ${balance:.2f}")
            self.updateAccounts()
        else:
            self.ui.label_top_t.setText("Insufficient funds.")
    
    # Write changes to the accounts.csv file when changes occur
    def updateAccounts(self):
        with open("accounts.csv", 'w') as file:
            file.write("Name,Pin,Balance\n")
            for account in self.accounts:
                file.write(f"{account['Name']},{account['Pin']},{float(account['Balance']):.2f}\n")

    # Navigation functions
    def gotoLogin(self):
        self.ui.errorLabel.setText("")
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
    def gotoMain(self):
        self.ui.label_top.setText(f"Welcome {self.accounts[self.current_account]['Name']}!")
        self.ui.stackedWidget.setCurrentWidget(self.ui.main)
    def gotoWithdraw(self):
        self.ui.inputLine_w.setText("")
        self.ui.label_top_w.setText("You are now withdrawing.")
        self.ui.label_bottom_w.setText("Please select an option.")
        self.ui.stackedWidget.setCurrentWidget(self.ui.withdraw)
    def gotoDeposit(self):
        self.ui.inputLine_d.setText("")
        self.ui.label_top_d.setText("You are now depositing.")
        self.ui.label_bottom_d.setText("Please select an option.")
        self.ui.stackedWidget.setCurrentWidget(self.ui.deposit)
    def gotoTransfer(self):
        self.ui.errorLabel_t.setText("")
        self.ui.inputLine_t.setText("")
        self.ui.label_top_t.setText("You are now transferring.")
        self.ui.label_bottom_t.setText("Please select an option.")
        self.ui.stackedWidget.setCurrentWidget(self.ui.transfer)
    def gotoBalance(self):
        self.ui.label_bottom_b.setText(f"${float(self.accounts[self.current_account]['Balance']):.2f}")
        self.ui.stackedWidget.setCurrentWidget(self.ui.balance)
    def gotoAccount(self):
        self.ui.label_top_a.setText(f"Owner: {self.accounts[self.current_account]['Name']}")
        self.ui.label_bottom_a.setText(f"Acct #/PIN: {self.accounts[self.current_account]['Pin']}")
        self.ui.stackedWidget.setCurrentWidget(self.ui.account)

    # Show the window (called initially in main.py)
    def show(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        self.main_window.show()
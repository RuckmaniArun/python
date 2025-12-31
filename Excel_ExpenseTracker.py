import os
from datetime import datetime
import openpyxl

tracker={
"expenses":[],
"savings":[]
}

def get_transaction_input():
	transaction_type=input("Enter transaction type: Savings/Expenses...")
	amount=input("How much spent?")
	category=input("Enter category..")
	description=input("Enter the description..")
	return transaction_type, amount, category, description

def add_transaction_ToExcel(transaction_type, amount, category, description):
	
	if os.path.exists("ExpenseTracker.xlsx"):
		wb=openpyxl.load_workbook("ExpenseTracker.xlsx")
		sheet=wb.active
		sheet.append([transaction_type,amount, category, description])
		wb.save("ExpenseTracker.xlsx")
	else:		
		wb=openpyxl.Workbook()
		sheet=wb.active
		sheet.append(["transaction_type", "amount", "category", "description"])
		sheet.append([transaction_type,amount, category, description])
		wb.save("ExpenseTracker.xlsx")
	print("Values are written to Excel")

	
def user_input():
	while(True):
		transaction_type, amount, category, description=get_transaction_input()
		add_transaction_ToExcel(transaction_type, amount, category, description)
		Repeat=input("Do you want to add another entry.. Y/N?")
		if Repeat=='Y':
			continue
		else:
			break
		
user_input()
#print(transaction_type, amount, category, description)
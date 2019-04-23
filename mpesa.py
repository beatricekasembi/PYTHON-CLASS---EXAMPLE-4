class MpesaAccount:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance

	def withdraw(self,b):
		withdraw = self.balance - b
		self.balance>b
		self.balance=self.balance-b

		statement="Dear {} of phone number {} your {} withdrawal has been processed and your current balance is {}.".format(self.name,self.phone_number,b,self.balance)
		
		print (statement)

	
	def deposit(self,b):
		deposit = self.balance + b
		self.balance=self.balance+b

		statement="Dear {} of phone number {} your {} deposit has been processed and your current balance is {}.".format(self.name,self.phone_number,b,self.balance)
		
		print (statement)


	def check_balance(self,b):
		check_balance = self.balance

		statement="Dear {} of phone number {} your current balance is {}".format(self.name,self.phone_number,self.balance)
		
		print (statement)

		



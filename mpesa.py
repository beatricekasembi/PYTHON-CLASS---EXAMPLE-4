class MpesaAccount:
	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = 0
		self.deposits=[]
		self.withdrawals=[]
		self.loan=0
		self.loan_repayment=loan_repayment



	def give_loan(self,p):

		if len(self.deposits)>=5 and p<1/3*sum (self.deposits) and self.loan==0;
			self.loan=self.loan+p
			print("Dear customer you qualify for a loan")

		else:
			print("Dear customer you do not qualify for a loan")


		def loan_repayment(self,x):

		if  self.loan-self.loan_repayment=x
			self.loan_repayment<self.loan
			
			print("Dear customer your loan repayment has been received.Your current loan balance is {} ".format(self.loan))

		else 

			self.loan_repayment>self.loan

			print("Dear customer your loan is fully settled.Your current loan balance is {} ".format(self.loan))



	def my_withdrawals(self):
		for x in self.withdrawals:
			print(x)

	def my_deposits(self):
		for y in self.deposits:
			print(y)

	def withdraw(self,b):
		if self.balance>b:
			self.balance=self.balance-b
			self.withdrawals.append(b)
			statement ="Dear {},phone number {} your {} withdrawal has been processed and your current balance is {}.".format(self.name,self.phone_number,b,self.balance)
			print (statement)

		else:
			print ("Insufficient balance")

	def deposit(self,b):
		deposit = self.balance + b
		self.balance=self.balance+b
		self.deposits.append(deposit)

		statement="Dear {} of phone number {} your {} deposit has been processed and your current balance is {}.".format(self.name,self.phone_number,b,self.balance)
		
		print (statement)


	def check_balance(self):
		check_balance = self.balance

		statement="Dear {} of phone number {} your current balance is {}".format(self.name,self.phone_number,self.balance)
		
		print (statement)

		



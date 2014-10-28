class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.penalty = 0
		
    def deposit(self, amount):
        """Deposits the amount into the account."""
       	self.balance += amount
       	return self.balance
       	
    def withdraw(self, amount):
    	if self.balance - amount < 0:
    		self.penalty += 5
    		self.balance -= amount+5
    	else:
    		self.balance -= amount
    	return self.balance
    	
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
       	self.balance -= amount
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.penalty
        




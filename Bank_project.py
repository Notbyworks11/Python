import logging

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        hold_balance =self.validate(balance)
        if hold_balance >=0:
            self._balance = hold_balance
        else:
            raise AttributeError('value must be > 0')
        
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner (self, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
            
        name = name.strip()
        if not name:
            raise ValueError("name cannot be empty")
        self._owner = name
        
    
    @property
    def balance(self):
        return self._balance
    
    def validate(self,value):
        if  isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError('value cannot be empty')
                
            try :
                value = float(value)
            except ValueError:
                raise ValueError('value must be a number')
            
        if isinstance(value,bool) or not isinstance(value,(int,float)):
            raise TypeError('value must be a number')
        
        
        return float(value)
        
    def deposit(self,value):
        
        amount=self.validate(value)    
        if  amount<= 0 :
            raise ValueError('value must be greater than zero')
        self._balance += amount
        
    def withdraw(self,value):
        amount=self.validate(value)
        if amount <= 0:
            raise ValueError('value cannot be negative')
            
        if amount > self._balance :
            raise ValueError('Amount cannot be more than balance \n Contact bank to include an overdraft')
           
        
        self._balance -= amount
#class Savings(Account):
 #   def __init__(self,name,)
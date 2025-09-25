import logging

class Account:
    def __init__(self,owner,amount):
        self.owner = owner
        self.amount = amount
        
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
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if  isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError('amount cannot be empty')
                
            try :
                value = float(value)
            except ValueError:
                raise TypeError('value must be an integer')
            
        if isinstance(value,bool) or not isinstance(value,(int,float)):
            raise ValueError('amount must be an integer')
        
            
        if value <= 0 :
            raise ValueError('amount must be greater than zero')
            
        self._amount = float(value)
        

p = Account("Andy",70)

print(p.amount)
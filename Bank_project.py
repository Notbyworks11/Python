import logging

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance
        
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
    

        
    def deposit(self,value):
        if  isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError('balance cannot be empty')
                
            try :
                value = float(value)
            except ValueError:
                raise TypeError('value must be an float')
            
        if isinstance(value,bool) or not isinstance(value,(int,float)):
            raise ValueError('balance must be an float')
        
            
        if value <= 0 :
            raise ValueError('balance must be greater than zero')
            
        self._balance += float(value)

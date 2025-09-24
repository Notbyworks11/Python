import os 
import hashlib

class User :
    def __init__(self , username , password):
        self.username = username
        self.password = password
        
    @property
    def password (self):
        raise AttributeError("Password is write-only")
        
    @password.setter
    def password (self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac("sha256",plaintext.encode("utf-8"), salt, 100_00)
        
        
        
trial = User("Andy","Hello1")
print(trial.password)
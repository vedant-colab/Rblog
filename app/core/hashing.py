from passlib.context import CryptContext

cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hasher:
    @staticmethod
    def hash_password(password):
        return cxt.hash(password)
        
    @staticmethod
    def verify_password(hashpassword, password):
        return cxt.verify(password, hashpassword)
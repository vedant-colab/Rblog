from passlib.context import CryptContext

cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hasher:
    @staticmethod
    def hash_password(password):
        # print(password, "in hash_password")
        return cxt.hash(password)
        # return "hi"
        
    @staticmethod
    def verify_password(hashpassword, password):
        return cxt.verify(password, hashpassword)
from passlib.context import CryptContext

bcrypy_context = CryptContext(schemes=['bcrypt'], deprecated= 'auto')

def hash_password(pwd: str):
    return bcrypy_context.hash(pwd)

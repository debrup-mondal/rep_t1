import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

user_input = input("Enter Password : ")

print(hash_password(user_input))
import random
import string

def generate_password():
    try:
        Len_pass = int(input("Enter the length of the password you want to generate: "))
        
        if Len_pass <= 0:
            print(" Password length must be greater than 0.")
            return
        
        Charaval = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        
        password = "".join(random.choice(Charaval) for _ in range(Len_pass))

        print("\n Your Generated Password:", password)
    
    except ValueError:
        print(" Invalid input! Please enter a valid number.")

generate_password()
import random
import string
def generate_pass():
    u=string.ascii_uppercase
    l=string.ascii_lowercase
    n=string.digits
    s="!@#$%&"
    password=[
        random.choice(u), random.choice(l), random.choice(n), random.choice(s)
    ]
    all_char=u+l+n+s
    while(len(password)<16):
        char=random.choice(all_char)
        if char not in password:
            password.append(char)
    
    random.shuffle(password)
    return "".join(password)
print("generate password", generate_pass())
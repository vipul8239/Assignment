def validate_ipv4(ip):
    
    parts = ip.split('.')
    if len(parts) != 4:
        return False, 

    for part in parts:
        if not part.isdigit():
            return False, 
        num = int(part)
        if num < 0 or num > 255:
            return False, 

    return True, 

def validate_gmail(email):
    
    if not email.endswith("@gmail.com"):
        return False, 

    username = email.split("@")[0]
    permitted_symbols = {'.', '+', '-', '_'}

    for char in username:
        if not (char.islower() or char.isdigit() or char in permitted_symbols):
            return False, 

    return True, 


if __name__ == "__main__":
    
    ip_address = input("Enter an IPv4 address to validate: ")
    ip_valid, ip_message = validate_ipv4(ip_address)
    print(ip_message)

    
    email_address = input("Enter an email address to validate: ")
    email_valid, email_message = validate_gmail(email_address)
    print(email_message)
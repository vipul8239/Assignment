def validate_ipv4(ip):
    """
    Validate if the given IP address is a valid IPv4 address.
    """
    parts = ip.split('.')
    if len(parts) != 4:
        return False, "Invalid IPv4 address. It must contain exactly 4 octets."

    for part in parts:
        if not part.isdigit():
            return False, "Invalid IPv4 address. All octets must be numeric."
        num = int(part)
        if num < 0 or num > 255:
            return False, "Invalid IPv4 address. Each octet must be between 0 and 255."

    return True, "Valid IPv4 address."

def validate_gmail(email):
    """
    Validate if the given email address is a valid Gmail address.
    """
    if not email.endswith("@gmail.com"):
        return False, "Invalid Gmail address. It must end with '@gmail.com'."

    username = email.split("@")[0]
    permitted_symbols = {'.', '+', '-', '_'}

    for char in username:
        if not (char.islower() or char.isdigit() or char in permitted_symbols):
            return False, "Invalid Gmail address. Username can only contain lowercase letters, numbers, or permitted symbols (., +, -, _)."

    return True, "Valid Gmail address."

# Main program
if __name__ == "__main__":
    # Validate IPv4 address
    ip_address = input("Enter an IPv4 address to validate: ")
    ip_valid, ip_message = validate_ipv4(ip_address)
    print(ip_message)

    # Validate Gmail address
    email_address = input("Enter an email address to validate: ")
    email_valid, email_message = validate_gmail(email_address)
    print(email_message)
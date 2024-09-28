"""
Ahmed Fadhil
"""

def main():
    password = get_valid_password()
    print_stars(len(password))

def get_valid_password():
    password = input("Password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = input("Password: ")

    return password

def print_stars(length):
    print("*" * length)

main()

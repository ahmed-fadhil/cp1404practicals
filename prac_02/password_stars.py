"""
Ahmed Fadhil
Wed 30 Oct 2024
"""

def main():
    password = get_password()
    print_stars(password)

def print_stars(password):
    length = len(password)
    print("*" * length)

def get_password():
    password = input("Password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = input("Password: ")
    return password


main()

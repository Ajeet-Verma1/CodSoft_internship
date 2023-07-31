import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            password_length = int(input("Enter the desired length of the password: "))
            if password_length <= 0:
                print("Password length must be greater than zero.")
                continue

            password = generate_password(password_length)
            print(f"Generated Password: {password}")

            choice = input("Do you want to generate another password? (y/n): ")
            if choice.lower() != 'y':
                print("Thank you for using the password generator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
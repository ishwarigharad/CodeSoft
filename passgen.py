import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    if length < 8:
        return "Password length should be at least 8 characters."

    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    """Main function to prompt user and display the generated password."""
    try:
        
        length = int(input("Enter the desired length of the password: ").strip())

        
        password = generate_password(length)

        
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")

if __name__ == "__main__":
    main()

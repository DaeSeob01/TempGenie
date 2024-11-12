from tempgenie.email_generator import generate_temp_email
from tempgenie.phone_generator import generate_temp_phone
from tempgenie.password_generator import suggest_password

def main():
    print("Welcome to TempGenie!")
    email = generate_temp_email()
    phone = generate_temp_phone()
    password = suggest_password()
    
    print(f"Generated Email: {email}")
    print(f"Generated Phone: {phone}")
    print(f"Suggested Password: {password}")

if __name__ == "__main__":
    main()

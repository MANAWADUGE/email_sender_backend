def is_valid_email(email):
    return '@' in email and '.' in email

while True:
    email_receiver = input("Enter the email receiver: ")
    if is_valid_email(email_receiver):
        print("Email receiver is valid.")
        break
    else:
        print("Error: Invalid email format. Please make sure to include both '@' and '.' symbols.")

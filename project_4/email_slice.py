# collect email from user
# Split the email using the @ the first part as user name
# second part will be domain
# Split domain using .,


def main():
    print("welcome to email slicer ")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"Username : {username} ")
    print(f"Domain: {domain} ")
    print(f"Extension: {extension} ")


main()

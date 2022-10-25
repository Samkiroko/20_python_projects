# collect email from user
# Split the email using the @ the first part as user name
# second part will be domain
# Split domain using .,


def main():
    print("welcome to email slicer ")

    email_input = input("Input your email address: ")

    if "@" in email_input and "." in email_input:

        if len(email_input.split("@")[1].split(".")) == 2:
            (username, domain) = email_input.split("@")
            (domain, extension) = domain.split(".")
            extension_2 = ""

        else:
            (username, domain) = email_input.split("@")
            (domain, extension, extension_2) = domain.split(".")

        print(f"Username : {username} ")
        print(f"Domain: {domain} ")
        print(f"Extension: {extension} ")
        print(f"Extension: {extension_2} ")
    else:
        print("Invalide email")


main()

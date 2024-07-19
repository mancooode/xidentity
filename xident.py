import faker

fake = faker.Faker()

def print_menu():
    print("""
▒██   ██▒ ██▓▓█████▄ ▓█████  ███▄    █ ▄▄▄█████▓ ██▓▄▄▄█████▓▓██   ██▓
▒▒ █ █ ▒░▓██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒ ▒██  ██▒
░░  █   ░▒██▒░██   █▌▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░  ▒██ ██░
 ░ █ █ ▒ ░██░░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██░░ ▓██▓ ░   ░ ▐██▓░
▒██▒ ▒██▒░██░░▒████▓ ░▒████▒▒██░   ▓██░  ▒██▒ ░ ░██░  ▒██▒ ░   ░ ██▒▓░
▒▒ ░ ░▓ ░░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▓    ▒ ░░      ██▒▒▒ 
░░   ░▒ ░ ▒ ░ ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░    ░     ▒ ░    ░     ▓██ ░▒░ 
 ░    ░   ▒ ░ ░ ░  ░    ░      ░   ░ ░   ░       ▒ ░  ░       ▒ ▒ ░░  
 ░    ░   ░     ░       ░  ░         ░           ░            ░ ░     
              ░                                               ░ ░     
XIDENTITY - Fake Identity Generator
------------------------------------

1. Generate a fake name
2. Generate a fake address
3. Generate a full fake identity

Choose an option: """)

def generate_name():
    print("Generated Name:")
    print(fake.name())

def generate_address():
    print("Generated Address:")
    print(fake.address())

def generate_full_identity():
    print("Generated Full Identity:")
    print("Name:", fake.name())
    print("Address:", fake.address())
    print("Email:", fake.email())
    print("Phone Number:", fake.phone_number())
    print("Job:", fake.job())

while True:
    print_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        generate_name()
    elif choice == "2":
        generate_address()
    elif choice == "3":
        generate_full_identity()
    else:
        print("Invalid option. Please choose again.")
    input("Press Enter to continue...")

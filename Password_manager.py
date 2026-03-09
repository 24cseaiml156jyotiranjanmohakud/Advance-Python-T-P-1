#Password Manager(securely store, edit, and retrieve user password using encroption)

class PasswordManager:

    def __init__(self):
        self.data = {}

    def encrypt(self, password):
        encrypted = ""
        for char in password:
            encrypted += chr(ord(char) + 3)
        return encrypted

    def decrypt(self, password):
        decrypted = ""
        for char in password:
            decrypted += chr(ord(char) - 3)
        return decrypted

    def add_password(self, website, username, password):
        encrypted_password = self.encrypt(password)
        self.data[website] = [username, encrypted_password]
        print("Password stored successfully")

    def retrieve_password(self, website):
        if website in self.data:
            username, encrypted_password = self.data[website]
            password = self.decrypt(encrypted_password)
            print("Website:", website)
            print("Username:", username)
            print("Password:", password)
        else:
            print("No record found")

    def update_password(self, website, new_password):
        if website in self.data:
            encrypted_password = self.encrypt(new_password)
            self.data[website][1] = encrypted_password
            print("Password updated successfully")
        else:
            print("Website not found")

    def delete_password(self, website):
        if website in self.data:
            del self.data[website]
            print("Password deleted successfully")
        else:
            print("Website not found")


manager = PasswordManager()

while True:

    print("\nPassword Manager")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Update Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        site = input("Enter Website: ")
        user = input("Enter Username: ")
        pwd = input("Enter Password: ")
        manager.add_password(site, user, pwd)

    elif choice == "2":
        site = input("Enter Website: ")
        manager.retrieve_password(site)

    elif choice == "3":
        site = input("Enter Website: ")
        new_pwd = input("Enter New Password: ")
        manager.update_password(site, new_pwd)

    elif choice == "4":
        site = input("Enter Website: ")
        manager.delete_password(site)

    elif choice == "5":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")
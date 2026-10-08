from User import User


class Twitter():
    def __init__(self):
        self.users = {}          # username -> User
        self.current_user = None

    def make_account(self, username, password):
        if username in self.users:
            print(f"Username '{username}' is already taken.")
            return None
        user = User(username, password)
        self.users[username] = user
        return user

    def login(self, username, password):
        user = self.users.get(username)
        if user is None or not user.check_password(password):
            print("Incorrect username or password.")
            return None
        self.current_user = user
        return user

    def logout(self):
        self.current_user = None


def main():
    twitter = Twitter()

    while True:
        if twitter.current_user is not None:
            print(f"\nLogged in as: {twitter.current_user.username}")
        else:
            print("\nNot logged in")
        print("1. Create account")
        print("2. Log in")
        print("3. View accounts")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            user = twitter.make_account(username, password)
            if user is not None:
                print(f"Account '{username}' created! You can now log in.")

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = twitter.login(username, password)
            if user is not None:
                print("\nLogged in! Here is your user description:")
                print(user)
            else:
                print("Login failed.")

        elif choice == "3":
            if not twitter.users:
                print("There are no accounts yet.")
                continue

            usernames = list(twitter.users)
            print("\nAccounts:")
            for i, name in enumerate(usernames, start=1):
                print(f"{i}. {name}")
            pick = input("Pick an account number (or press Enter to go back): ").strip()
            if pick == "":
                continue
            if not pick.isdigit() or not 1 <= int(pick) <= len(usernames):
                print("Invalid account number.")
                continue

            user = twitter.users[usernames[int(pick) - 1]]
            print()
            if user is twitter.current_user:
                print(user)            # your own account: show everything
            else:
                print(user.public_info())   # someone else's: hide the password

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()

from User import User
from Post import Post
from Feed import Feed
import json
from pathlib import Path
from Exceptions import AccountNotFoundError

class Twitter():
    def __init__(self):
        self.users = {}          # username -> User
        self.current_user = None


    def save_data(self, filename="twitter_data.json"):
        data = {}

        for username, user in self.users.items():
            data[username] = {
                "password": user.password,
                "followers": [u.username for u in user.followers],
                "following": [u.username for u in user.following],
                "posts": [
                    {"author": p.author, "text": p.text}
                    for p in user.posts
                ]
            }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, filename="twitter_data.json"):
        if not Path(filename).exists():
            return

        with open(filename, "r") as file:
            data = json.load(file)

        for username, info in data.items():
            self.users[username] = User(
                username, info["password"]
            )

        for username, info in data.items():
            user = self.users[username]

            user.following = [
                self.users[name]
                for name in info["following"]
            ]

            user.followers = [
                self.users[name]
                for name in info["followers"]
            ]

            user.posts = [
                Post(p["author"], p["text"])
                for p in info["posts"]
            ]

    
    
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

    def get_user(self, username):
        if username not in self.users:
            raise AccountNotFoundError(
                f"Account '{username}' does not exist."
            )

        return self.users[username]

def main():
    twitter = Twitter()
    twitter.load_data()

    while True:
        if twitter.current_user is not None:
            print(f"\nLogged in as: {twitter.current_user.username}")
        else:
            print("\nNot logged in")
        print("1. Create account")
        print("2. Log in")
        print("3. Create post")
        print("4. View accounts")
        print("5. Follow user")
        print("6. Unfollow user")
        print("7. Check following status")
        print("8. View feed")
        print("9. Quit")
        choice = input("Choose an option: ").strip()


        if choice == "1":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            user = twitter.make_account(username, password)
            if user is not None:
                print(f"Account '{username}' created! You can now log in.")
                twitter.save_data()

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
            if twitter.current_user is not None:
                post_text = input("what are your thoughts?: ")
                new_post = Post(twitter.current_user.username, post_text)
                twitter.current_user.posts.append(new_post)
                twitter.save_data()
                print("Post published!")
            else:
                print("Please log in before you post! ")
                continue

        elif choice == "4":
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

        
        elif choice == "5":
            if twitter.current_user is None:
                print("Please log in first.")
                continue

            username = input("Who do you want to follow? ")

            try:
                other_user = twitter.get_user(username)

                if twitter.current_user.follow(other_user):
                    print(f"You followed {username}!")
                    twitter.save_data()
                else:
                    print("Unable to follow this account.")

            except AccountNotFoundError as error:
                print(error)


        
        
        elif choice == "6":
            if twitter.current_user is None:
                print("Please log in first.")
                continue

            username = input("Who do you want to unfollow? ")

            try:
                other_user = twitter.get_user(username)

                if twitter.current_user.unfollow(other_user):
                    print(f"You unfollowed {username}!")
                    twitter.save_data()
                else:
                    print(f"You are not following {username}.")

            except AccountNotFoundError as error:
                print(error)


        elif choice == "7":
            if twitter.current_user is None:
                print("Please log in first.")
                continue

            username = input("Enter username: ")
            other_user = twitter.users.get(username)

            if other_user is None:
                print("Account does not exist.")
            elif twitter.current_user.is_following(other_user):
                print(f"You are following {username}.")
            else:
                print(f"You are not following {username}.")

        elif choice == "8":
            if twitter.current_user is None:
                print("Please log in first.")
                continue

            feed = Feed(twitter.current_user)
            feed.show_feed()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1 through 9.")



if __name__ == "__main__":
    main()

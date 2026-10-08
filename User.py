class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.posts = []

    def check_password(self, password):
        """Return True if the given password matches this user's password."""
        return self.password == password

    def public_info(self):
        """Return the user's details without the password (for viewing other accounts)."""
        return (f"Username: {self.username}\n"
                f"Followers: {self.followers}\n"
                f"Following: {self.following}\n"
                f"Posts: {self.posts}")

    def __repr__(self):
        return (f"Username: {self.username}\n"
                f"Password: {self.password}\n"
                f"Followers: {self.followers}\n"
                f"Following: {self.following}\n"
                f"Posts: {self.posts}")

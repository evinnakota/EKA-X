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
        return (f"Username: {self.username}\n"
                f"Followers: {[user.username for user in self.followers]}\n"
                f"Following: {[user.username for user in self.following]}\n"
                f"Posts: {self.posts}")


    def show_posts(self):
        for post in self.posts:
            print(post.show_post())

    def follow(self, other_user):
        if self == other_user:
            return False
        if other_user in self.following:
            return False
        self.following.append(other_user)
        other_user.followers.append(self)
        return True

    def unfollow(self,other_user):
        if other_user not in self.following:
            return False
        self.following.remove(other_user)
        other_user.followers.remove(self)
        return True

    def is_following(self, other_user):
        return other_user in self.following

    def __repr__(self):
            return self.public_info()

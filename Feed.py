class Feed():
    def __init__(self,user):
        self.user = user
    def get_posts(self):
        posts = []

        for followed_user in self.user.following:
            for post in followed_user.posts:
                posts.append(post)

        return posts
    
    def show_feed(self):
        posts = self.get_posts()

        if not posts:
            print("Your feed is empty.")
            return

        for post in posts:
            print(post.show_post())
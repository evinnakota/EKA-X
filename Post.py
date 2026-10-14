class Post():
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def show_post(self):
        return (
            f"Post: {self.text}\n" 
            f"Author: {self.author}\n"
                )

    def __repr__(self):
        return self.show_post()
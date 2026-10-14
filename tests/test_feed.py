
from User import User
from Post import Post
from Feed import Feed

def test_empty_feed():
    alice = User("alice", "123")
    feed = Feed(alice)

    assert feed.get_posts() == []

def test_followed_user_posts():
    alice = User("alice", "123")
    bob = User("bob", "456")

    alice.follow(bob)
    post = Post("bob", "Hello world!")
    bob.posts.append(post)

    feed = Feed(alice)

    assert feed.get_posts() == [post]

def test_multiple_followed_users():
    alice = User("alice", "123")
    bob = User("bob", "456")
    charlie = User("charlie", "789")

    alice.follow(bob)
    alice.follow(charlie)

    post1 = Post("bob", "Hello!")
    post2 = Post("charlie", "Hi!")

    bob.posts.append(post1)
    charlie.posts.append(post2)

    feed = Feed(alice)

    assert post1 in feed.get_posts()
    assert post2 in feed.get_posts()

def test_unfollow_removes_posts():
    alice = User("alice", "123")
    bob = User("bob", "456")

    alice.follow(bob)
    bob.posts.append(Post("bob", "Hello!"))

    feed = Feed(alice)
    alice.unfollow(bob)

    assert feed.get_posts() == []

def test_unfollowed_user_posts_hidden():
    alice = User("alice", "123")
    bob = User("bob", "456")

    bob.posts.append(Post("bob", "Hello!"))

    feed = Feed(alice)

    assert feed.get_posts() == []

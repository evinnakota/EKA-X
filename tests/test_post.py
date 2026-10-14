
from Twitter import Twitter
from Post import Post


def test_create_post():
    post = Post("alice", "Hello world!")

    assert post.author == "alice"
    assert post.text == "Hello world!"


def test_show_post():
    post = Post("alice", "Hello world!")

    expected = "Post: Hello world!\nAuthor: alice\n"

    assert post.show_post() == expected


def test_post_repr():
    post = Post("alice", "Hello!")

    assert repr(post) == post.show_post()


def test_add_post_to_user():
    twitter = Twitter()
    alice = twitter.make_account("alice", "123")

    post = Post(alice.username, "My first post!")
    alice.posts.append(post)

    assert len(alice.posts) == 1
    assert alice.posts[0] == post


def test_multiple_posts():
    twitter = Twitter()
    alice = twitter.make_account("alice", "123")

    post1 = Post("alice", "First post")
    post2 = Post("alice", "Second post")

    alice.posts.append(post1)
    alice.posts.append(post2)

    assert len(alice.posts) == 2
    assert alice.posts[0] == post1
    assert alice.posts[1] == post2


def test_posts_belong_to_correct_user():
    twitter = Twitter()

    alice = twitter.make_account("alice", "123")
    bob = twitter.make_account("bob", "456")

    post = Post("alice", "Hello!")
    alice.posts.append(post)

    assert post in alice.posts
    assert post not in bob.posts


def test_show_user_posts(capsys):
    twitter = Twitter()
    alice = twitter.make_account("alice", "123")

    alice.posts.append(Post("alice", "Hello!"))
    alice.show_posts()

    output = capsys.readouterr().out

    assert "Hello!" in output
    assert "alice" in output

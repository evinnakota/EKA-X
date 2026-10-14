
from Twitter import Twitter


def test_create_account():
    twitter = Twitter()

    user = twitter.make_account("alice", "123")

    assert user is not None
    assert user.username == "alice"
    assert "alice" in twitter.users


def test_duplicate_username():
    twitter = Twitter()

    twitter.make_account("alice", "123")
    duplicate = twitter.make_account("alice", "456")

    assert duplicate is None
    assert len(twitter.users) == 1


def test_login_success():
    twitter = Twitter()

    twitter.make_account("alice", "123")
    user = twitter.login("alice", "123")

    assert user is not None
    assert twitter.current_user == user


def test_login_wrong_password():
    twitter = Twitter()

    twitter.make_account("alice", "123")
    user = twitter.login("alice", "wrong")

    assert user is None
    assert twitter.current_user is None


def test_login_nonexistent_user():
    twitter = Twitter()

    user = twitter.login("nobody", "123")

    assert user is None
    assert twitter.current_user is None


def test_logout():
    twitter = Twitter()

    twitter.make_account("alice", "123")
    twitter.login("alice", "123")
    twitter.logout()

    assert twitter.current_user is None


def test_accounts_have_separate_data():
    twitter = Twitter()

    alice = twitter.make_account("alice", "123")
    bob = twitter.make_account("bob", "456")

    assert alice != bob
    assert alice.followers == []
    assert bob.followers == []
    assert alice.posts == []
    assert bob.posts == []

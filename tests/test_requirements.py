
import pytest
import os

from Twitter import Twitter
from Post import Post
from Exceptions import AccountNotFoundError


TEST_FILE = "test_data.json"


def test_save_and_load_accounts():
    twitter = Twitter()
    twitter.make_account("alice", "123")
    twitter.save_data(TEST_FILE)

    new_twitter = Twitter()
    new_twitter.load_data(TEST_FILE)

    assert "alice" in new_twitter.users
    assert new_twitter.users["alice"].check_password("123")


def test_save_and_load_posts():
    twitter = Twitter()
    alice = twitter.make_account("alice", "123")
    alice.posts.append(Post("alice", "Hello world!"))

    twitter.save_data(TEST_FILE)

    new_twitter = Twitter()
    new_twitter.load_data(TEST_FILE)

    posts = new_twitter.users["alice"].posts

    assert len(posts) == 1
    assert posts[0].author == "alice"
    assert posts[0].text == "Hello world!"


def test_save_and_load_following():
    twitter = Twitter()
    alice = twitter.make_account("alice", "123")
    bob = twitter.make_account("bob", "456")

    alice.follow(bob)
    twitter.save_data(TEST_FILE)

    new_twitter = Twitter()
    new_twitter.load_data(TEST_FILE)

    loaded_alice = new_twitter.users["alice"]
    loaded_bob = new_twitter.users["bob"]

    assert loaded_bob in loaded_alice.following
    assert loaded_alice in loaded_bob.followers


def test_load_missing_file():
    twitter = Twitter()
    twitter.load_data("nonexistent_test_file.json")

    assert twitter.users == {}


def test_get_existing_account():
    twitter = Twitter()
    alice = twitter.make_account("alice", "123")

    assert twitter.get_user("alice") is alice


def test_account_not_found_exception():
    twitter = Twitter()

    with pytest.raises(AccountNotFoundError):
        twitter.get_user("nobody")


def teardown_module(module):
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

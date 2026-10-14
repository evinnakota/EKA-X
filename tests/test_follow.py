
from User import User

def test_follow_user():
    alice = User("alice", "123")
    bob = User("bob", "456")

    assert alice.follow(bob) == True
    assert bob in alice.following
    assert alice in bob.followers

def test_unfollow_user():
    alice = User("alice", "123")
    bob = User("bob", "456")

    alice.follow(bob)
    assert alice.unfollow(bob) == True
    assert bob not in alice.following
    assert alice not in bob.followers

def test_cannot_follow_self():
    alice = User("alice", "123")

    assert alice.follow(alice) == False

def test_cannot_follow_twice():
    alice = User("alice", "123")
    bob = User("bob", "456")

    alice.follow(bob)
    assert alice.follow(bob) == False
    assert alice.following.count(bob) == 1

def test_is_following():
    alice = User("alice", "123")
    bob = User("bob", "456")

    assert alice.is_following(bob) == False
    alice.follow(bob)
    assert alice.is_following(bob) == True

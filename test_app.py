from app import greet, add_one


def test_greet():
    assert greet("Dave") == "Howsit, Dave!"


def test_add_one():
    assert add_one(3) == 4


print(greet("Dave"))
print(add_one(3))

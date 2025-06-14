from app import say_hello, add_one


def test_say_hello():
    assert say_hello("Dave") == "Hello, Dave!"


def test_add_one():
    assert add_one(3) == 4


print(say_hello("Dave"))
print(add_one(3))

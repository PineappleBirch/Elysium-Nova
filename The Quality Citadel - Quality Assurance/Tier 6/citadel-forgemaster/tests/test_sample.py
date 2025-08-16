def test_addition():
    """
    A simple test that should pass.
    """
    assert 1 + 1 == 2

def test_subtraction():
    """
    A simple test that is designed to fail.
    """
    assert 5 - 2 == 4, "Subtraction failed: Expected 3"

def test_string_uppercase():
    """
    Another simple test that should pass.
    """
    assert "hello".upper() == "HELLO"
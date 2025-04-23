import pytest


def add_foo(a, b):
    """Add two numbers."""
    return a + b


def test_add_foo():
    """Test the add_foo function."""
    assert add_foo(1, 2) == 3
    assert add_foo(-1, 1) == 0
    assert add_foo(0, 0) == 0
    assert add_foo(-1, -1) == -2


@pytest.mark.parametrize("a,b,expected", [(1,2,3), (2,3,5)])
def test_add_parametrized(a, b, expected):
    """Test the add_foo function with parametrization."""
    assert add_foo(a, b) == expected


def divide_foo(a, b):
    """Divide two numbers."""
    return a / b


def test_divide_foo():
    """Test the divide_foo function."""
    assert divide_foo(1, 2) == 0.5
    assert divide_foo(-1, 1) == -1
    assert divide_foo(0, 1) == 0
    assert divide_foo(-1, -1) == 1


def test_divide_foo_zero_division():
    """Test the divide_foo function for zero division."""
    with pytest.raises(ZeroDivisionError):
        divide_foo(1, 0)


# Define a fixture
@pytest.fixture
def resource():
    return {"koko": "bebe"}

# Use the fixture in a test
def test_resource_key(resource):
    assert resource["koko"] == "bebe"

def test_resource_type(resource):
    assert isinstance(resource, dict)

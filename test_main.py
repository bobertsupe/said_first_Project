from main import add
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Additional test cases can be added as needed
    assert add(2.5, 2.5) == 5.0 
    assert add(-2, -3) == -5 
    assert add(1000, 2000) == 3000


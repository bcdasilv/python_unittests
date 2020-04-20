import pytest 

def sum(a, b):
    return a + b

def contains_numbers(alpha_num_str):
    for char in alpha_num_str:
        if char.isdigit():
            return True 
    return False

def test_sum():
    num1 = 5
    num2 = 10
    expected = 15
    assert sum(num1, num2) == 15

def test_contains_numbers():
    input_str = "el12lk3j5mnfadf"
    assert contains_numbers(input_str) == True

def test_does_not_contain_numbers():
    input_str = "lkqwjqlkjlkjed"
    assert contains_numbers(input_str) == False

def div(a, b):
    return a / b

def test_div():
    num1 = 10
    num2 = 5
    expected = 2
    assert div(num1, num2) == expected

def test_div_by_zero():
    num1 = 10
    num2 = 0
    with pytest.raises(ZeroDivisionError):
        div(num1, num2)

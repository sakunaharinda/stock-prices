import pytest
from test_stock_prices import max_difference


# This unit test tests the success scenario with one maximum difference (10-2 = 8)
def test_max_difference_success():
    arr = [2,3,4,10,9]
    diff = max_difference(arr)
    assert diff==8

# This unit test tests the success scenario with multiple occurances of maximum difference (10-2 = 8 and 10-2=8)
def test_max_difference_multiple_max_profits_success():
    arr = [2,5,10,3,4,10]
    diff = max_difference(arr)
    assert diff==8

# This unit test tests the function with an empty array (Index error will be thrown)
def test_max_difference_empty_arr_failed():
    arr = []
    with pytest.raises(IndexError) as exec_info:
        diff = max_difference(arr)
    assert "list index out of range" in str(exec_info.value)

# This unit test tests the function with an array with non-numeric characters (Type error will be thrown)
def test_max_difference_arr_with_string_failed():
    arr = [1,2,'a']
    with pytest.raises(TypeError) as exec_info:
        diff = max_difference(arr)
    assert "'<' not supported between instances of 'str' and 'int'" in str(exec_info.value)

# This unit test tests the function with a string instead of an array (Type error will be thrown)
def test_max_difference_string_failed():
    arr = '1234'
    with pytest.raises(TypeError) as exec_info:
        diff = max_difference(arr)
    assert "unsupported operand type(s) for -: 'str' and 'str'" in str(exec_info.value)



import pytest

def max_difference(sp):
        min_price = sp[0]
        max_diff = sp[1]-sp[0]
        for price in sp:
            if price<min_price:
                min_price = price
            elif max_diff < price-min_price:
                max_diff = price - min_price
        return max_diff


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

# This unit test tests the success scenario with decreasing stock prices
def test_max_difference_decreasing_prices():
    arr = [5,4,3,2,1]
    diff = max_difference(arr)
    assert diff==0
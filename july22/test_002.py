# assertions

# >Way of validating the tests
# • Use operators like ==, !=, <=, >= for asserting.
# • You can use the above operators for validating strings and numbers.
# • assert 1, means assert True
# • assert 0, means assert False. This is going to fail your test.
# • In Python, multiplication, division has higher precedence than add, subtract.
# • assert with ‘in’ operator to validate if a value is within a tuple, list or string.
# • Good Test writing Practice: Try to add only 1 assert in single test.

def test_addition():
    assert 1+1 == 2


def test_subraction():
    assert 3-1 == 4
# import isvalid function from valid parenthesis.py here   

from Python.valid_parenthesis import isValid    # import the function from the file 

def test_isValid():
    # Test cases with valid parentheses
    assert isValid("") == True
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("{[]}") == True
    assert isValid("[{()}]") == True

    # Test cases with invalid parentheses
    assert isValid("(") == False
    assert isValid(")") == False
    assert isValid("([)]") == False
    assert isValid("{[}]") == False
    assert isValid("{{{{") == False

    print("All test cases passed!")

test_isValid()
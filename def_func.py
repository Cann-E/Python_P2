def raise_both(value1,value2):
    """Raise Value1 to the power of the value2 and vice versa"""  #DOCSTRING
    
    new_val1=value1**value2
    
    new_val2=value2**value1
    
    new_tuple=(new_val1,new_val2)
    
    return new_tuple


print(raise_both(5,9))
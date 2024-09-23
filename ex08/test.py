#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import frontal_function, MySpecificException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert frontal_function("3 Fizz 5 Buzz 15") == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz"
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises():
        frontal_function()
    ###
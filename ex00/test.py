#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import helloworld, TooLongException
 
def testHelloworld():
    
    ### Nominal Cases
    assert helloworld("fr","Alice") == "Bonjour Alice"
    assert helloworld("en","Bob") == "Hello Bob"
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(TooLongException):
        helloworld("en","abcdefghijklmnopq")
    ###
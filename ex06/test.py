#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import frontal_function, MySpecificException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert frontal_function(...) == ...
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(...):
        frontal_function(...)
    ###
#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import frontal_function, MySpecificException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert frontal_function("Je vais sur un bateau qui est sur la mer") == "bateau:1,est:1,je:1,la:1,mer:1,qui:1,sur:2,un:1,vais:1"
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises():
        frontal_function("")
    ###
#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import frontal_function, MySpecificException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    def test_dna_to_rna():
    ### Nominal Cases
    # Séquence ADN valide, avec conversion en ARN
    assert dna_to_rna("acgt") == "ACGU"
    assert dna_to_rna("ACGT") == "ACGU"
    assert dna_to_rna("aTcG") == "AUCg"
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(...):
        frontal_function(...)
    ###
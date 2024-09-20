# test_main.py

import pytest
from main import frontal_function, MySpecificException

def test_frontal_function():
    ### Nominal Cases
    # Test avec des valeurs typiques
    assert frontal_function(1.0, 1.0) == 0.84714
    assert frontal_function(2.0, 3.0) == 0.73268
    assert frontal_function(-1.0, -1.0) == 0.84714
    assert frontal_function(0.5, 0.5) == 0.91667

    ### Edge cases and corner cases
    # Test avec des valeurs qui devraient lever une exception
    with pytest.raises(MySpecificException, match="ARITHMETIC ERROR"):
        frontal_function(0, 1)
    
    with pytest.raises(MySpecificException, match="ARITHMETIC ERROR"):
        frontal_function(1, 0)

    with pytest.raises(MySpecificException, match="ARITHMETIC ERROR"):
        frontal_function(0, 0)

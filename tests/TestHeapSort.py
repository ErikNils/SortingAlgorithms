#!/usr/bin/python3


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from SortingAlgorithms.HeapSort import heapSort


@pytest.mark.parametrize('call_par')
def test_math(call_par):
    
    (old_value, new_value, equals) = call_par.split(';')
    print("it is " + equals + " that " + old_value + " is equal to " + new_value)
    assert old_value == new_value



if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_", "-v", "-s"])
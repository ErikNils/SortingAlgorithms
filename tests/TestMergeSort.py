#!/usr/bin/python3


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hypothesis import given, assume, strategies as st
from SortingAlgorithms.MergeSort import mergeSort


@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    print("Unsorted: " + str(xs))
    xs = sorted(xs)
    mergeSort(ys)
    
    print("xs: " + str(xs))
    print("ys: " + str(ys))
    
    assert xs == ys
    
    
if __name__ == "__main__":
    test_reversing_twice_gives_same_list()
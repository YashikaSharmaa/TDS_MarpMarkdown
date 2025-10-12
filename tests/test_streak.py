import pytest
from streak.streak import detect_streaks

def test_empty_list():
    assert detect_streaks([]) == []

def test_no_positive_numbers():
    assert detect_streaks([-1, -2, 0, -5]) == []

def test_all_positive_numbers():
    assert detect_streaks([1, 2, 3, 4, 5]) == [[1, 2, 3, 4, 5]]

def test_single_streak():
    assert detect_streaks([-1, 0, 1, 2, 3, 0, -2]) == [[1, 2, 3]]

def test_multiple_streaks():
    assert detect_streaks([1, 2, 0, 3, 4, -5, 6]) == [[1, 2], [3, 4], [6]]

def test_streaks_at_beginning_and_end():
    assert detect_streaks([1, 2, -1, 0, 3, 4]) == [[1, 2], [3, 4]]

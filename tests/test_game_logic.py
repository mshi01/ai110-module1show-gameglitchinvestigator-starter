import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"

def test_hints_not_backwards():
    # Regression test: hints were previously swapped (high→"Too Low", low→"Too High")
    # A guess ABOVE the secret must say "Too High", not "Too Low"
    high_result = check_guess(75, 50)
    assert high_result[0] == "Too High", f"Expected 'Too High' for guess 75 > secret 50, got {high_result[0]!r}"

    # A guess BELOW the secret must say "Too Low", not "Too High"
    low_result = check_guess(25, 50)
    assert low_result[0] == "Too Low", f"Expected 'Too Low' for guess 25 < secret 50, got {low_result[0]!r}"

"""Entrypoint

Usage example:
    python main.py (this runs all tests)
    python main.py day1 (this runs all tests in day1)
"""

import sys

import pytest

if __name__ == "__main__":
    # get input from argument
    day_number = sys.argv[1] if len(sys.argv) > 1 else "."

    pytest.main(["-rP", day_number])

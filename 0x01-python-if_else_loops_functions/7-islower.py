#!/usr/bin/env python3
def islower(c):
    """Checks if a given character is lowercase."""
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False

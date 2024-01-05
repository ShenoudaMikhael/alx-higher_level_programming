#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns the length of astring and first Character."""
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)

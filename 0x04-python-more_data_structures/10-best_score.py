#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key associated with the highest value in a dictionary."""
    # return max(a_dictionary, key=lambda k: a_dictionary[k])
    if a_dictionary:
        m_key = ""
        m_value = 0
        for k, v in a_dictionary.items():
            m_key = k if v > m_value else m_key
            m_value = v if v > m_value else m_value
        return m_key

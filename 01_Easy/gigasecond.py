from datetime import timedelta
"""
Given a moment, determine the moment that would be after a gigasecond has passed.
A gigasecond is 10^9 (1,000,000,000) seconds.
"""
def add(moment):
    return moment + timedelta(seconds=10**9)

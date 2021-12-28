"""
Bob's conversational partner is a purist when it comes to written communication
and always follows normal rules regarding sentence punctuation in English.
"""
def response(hey_bob):
    hey_bob=hey_bob.strip()
    # Bob answers 'Sure.' if you ask him a question, such as "How are you?".
    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    # He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    # He answers 'Calm down, I know what I'm doing!' if you yell a question at him
    elif not hey_bob:
        return "Fine. Be that way!"
    # He answers 'Whatever.' to anything else.
    else:
        return "Whatever."

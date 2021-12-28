# Import numpy library
import statistics

# Implement a function that takes the current round numbe
# and returns a single list with that round and the next two that are coming up:
def get_rounds(number):
    """
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    return [number,number + 1,number + 2]

# Implement a function that takes two lists and returns a single list
#consisting of all the rounds in the first list,
# followed by all the rounds in the second list:
def concatenate_rounds(rounds_1, rounds_2):
    """
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2

# Implement a function that takes two arguments,
# a list of rounds played and a round number.
# The function will return True if the round is in the list of rounds played,
# False if not:
def list_contains_round(rounds, number):
    """
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds

# Implement a function that will return the average value of a hand of Black Joe.
def card_average(hand):
    """
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return statistics.mean(hand)

# Implement a function that returns a Boolean.
# The function should return True if one (or both) of Elyse's approximations
# yields the same value as calculating the "full" average of a hand.
# The function should return False if neither approximation formula
# yields the same value as the "full" average.
# For the sake of a simple median, we are going to assume the hand always has an odd number of card values.
def approx_average_is_average(hand):
    """
    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """
    approx_average1 = (hand[0] + hand[-1]) / 2
    approx_average2 = hand[(len(hand)) // 2 ]
    return card_average(hand) in (approx_average1, approx_average2)

# Implement a function that returns a Boolean indicating
#if the average of the cards at even indexes is the same as the average of the cards at odd indexes.
def average_even_is_average_odd(hand):
    """
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even = hand[0::2]
    odd = hand[1::2]
    return card_average(even) == card_average(odd)

# Implement a function that takes a hand and checks if the last card is a Jack (11).
#If the the last card is a Jack (11), double its value before returning the hand.
def maybe_double_last(hand):
    """
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1]= hand[-1]*2
    return hand

# Define the eat_ghost() function that takes two parameters
# (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost)
# and returns a Boolean value if Pac-Man is able to eat the ghost.
# The function should return True only if Pac-Man has a power pellet active and is touching a ghost.
def eat_ghost(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if power_pellet_active and touching_ghost:
        return True
    return False

# Define the score() function that takes two parameters
# (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot)
# and returns a Boolean value if Pac-Man scored.
# The function should return True if Pac-Man is touching a power pellet or a dot.
def score(touching_power_pellet, touching_dot):
    """
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    if touching_power_pellet or touching_dot:
        return True
    return False

# Define the lose() function that takes two parameters
# (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost)
# and returns a Boolean value if Pac-Man loses.
# The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.
def lose(power_pellet_active, touching_ghost):
    """
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    if not power_pellet_active and touching_ghost:
        return True
    return False

# Define the win() function that takes three parameters
# (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is touching a ghost)
# and returns a Boolean value if Pac-Man wins.
# The function should return True if Pac-Man has eaten all of the dots
# and has not lost based on the parameters defined in part 3.
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    lost = lose(power_pellet_active,touching_ghost)
    if has_eaten_all_dots and not lost:
        return True
    return False

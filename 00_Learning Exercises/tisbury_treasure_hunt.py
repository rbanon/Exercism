"""
Azara and Rui are teammates competing in a pirate-themed treasure hunt.
One has a list of treasures with map coordinates, the other a list of location names with map coordinates.
They've also been given blank maps with a starting place marked YOU ARE HERE.
"""

# Takes a (treasure, coordinate) pair from Azara's list and returns only the extracted map coordinate.
def get_coordinate(record):
    """
    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]

# Takes a coordinate in the format "2A" and returns a tuple in the format ("2", "A").
def convert_coordinate(coordinate):
    """
    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """
    return tuple(coordinate)

# Takes a (treasure, coordinate) pair and a (location, coordinate, quadrant) record
# and compares coordinates from each.
# Return True if the coordinates "match", and return False if they do not.
# Re-format coordinates as needed for accurate comparison.
def compare_records(azara_record, rui_record):
    """
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    return convert_coordinate(azara_record[1]) == rui_record[1]

# Takes a (treasure, coordinate) pair from Azara's list and a
# (location, coordinate, quadrant) record from Rui's list
# and returns (treasure, coordinate, location, coordinate, quadrant) if the coordinates match.
# If the coordinates do not match, return the string "not a match".
# Re-format the coordinate as needed for accurate comparison.
def create_record(azara_record, rui_record):
    """
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"

# Clean up the combined records from Azara and Rui so that there's only one set of coordinates per record
def clean_up(combined_record_group):
    """
    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    clean = ""
    for a_tuple in combined_record_group:
        new_tuple = tuple([a_tuple[0]]) + tuple(a_tuple[2:])
        clean +=  str(new_tuple) + "\n"
    return clean
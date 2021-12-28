# Implement the function which takes a title str as a parameter and capitalizes the first letter of each word.
# This function should return a str in title case.
def capitalize_title(title):
    """
    :param title: str title string that needs title casing
    :return:  str title string in title case (first letters capitalized)
    """
    return title.title()

# Implement the function that takes sentence as a parameter.
def check_sentence_ending(sentence):
    """
    :param sentence: str a sentence to check.
    :return:  bool True if punctuated correctly with period, False otherwise.
    """
    return sentence[-1] == "."

# Implement the function that takes sentence as a parameter.
# The function should remove extra whitespace at both the beginning and the end of the sentence,
# returning a new, updated sentence str.
def clean_up_spacing(sentence):
    """
    :param sentence: str a sentence to clean of leading and trailing space characters.
    :return: str a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()

# Write the function that takes sentence, old_word, and new_word as parameters.
# This function should replace all instances of the old_word with the new_word,
# and return a new str with the updated sentence.
def replace_word_choice(sentence, old_word, new_word):
    """
    :param sentence: str a sentence to replace words in.
    :param old_word: str word to replace
    :param new_word: str replacement word
    :return:  str input sentence with new words in place of old words
    """
    return sentence.replace(old_word,new_word)

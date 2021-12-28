# Implement the add_prefix_un() function that takes word as a parameter and returns a new un prefixed word:
def add_prefix_un(word):
    """
    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return "un"+word

# Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form:
# [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like:
# '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.
# EX: make_word_groups(['en', 'close', 'joy', 'lighten'])
def make_word_groups(vocab_words):
    """
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with prefix applied, separated by ' :: '.
    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    prefix = vocab_words[0]
    return prefix+" :: "+" :: ".join([prefix + i for i in vocab_words[1:]])

#  the remove_suffix_ness(<word>) function that takes in a word str, and returns the root word without the ness suffix.
def remove_suffix_ness(word):
    """
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
    This function takes in a word and returns the base word with `ness` removed.
    """
    if word.endswith('iness'):
        base = word[:-5]+"y"
    else:
        base = word[:-4]
    return base

# Implement the noun_to_verb(<sentence>, <index>) function that takes two parameters.
# A sentence using the vocabulary word, and the index of the word, once that sentence is split apart.
#The function should return the extracted adjective as a verb.
def noun_to_verb(sentence, index):
    """
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    if sentence[-1] == ".":
        sentence = sentence[:-1]

    nouns = sentence.split()
    verb = nouns[index]+"en"
    return verb

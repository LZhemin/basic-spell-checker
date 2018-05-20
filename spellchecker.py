import os
import sys
import re
import collections

# set of alphabets of concern
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w,', 'x', 'y', 'z'}


def get_freq():
    """
    Function to build a dictionary of word and its frequency in the corpus

    Args:

    Returns:
        defaultdictionary<str,int>
        corpus of words and its frequency in the corpus.
    """
    path = os.path.join(os.getcwd(), 'data')
    model = collections.defaultdict(lambda: 0)
    for root, dirs, files in os.walk(path):
        for _file in files:
            file_path = os.path.join(path, _file)
            model = train(model, words(open(file_path).read()))
    return model


def words(text):
    """
    Function to process the text and check if the text made up of english alphabet

    Args:
        text: (str) word to match against the Regex
    Returns:
        list<str>
        words that matched the regex
    """
    return re.findall('[a-z]+', text.lower())


def train(model, features):
    """
    Function to update frequency count of a word

    Args:
        model:      (defaultdictionary<str,int>) to be updated
        features:   (str) word to increment
    Returns:
        defaultdictionary<str,int>
        Updated corpus of words and its frequency in the corpus.
    """
    for f in features:
        model[f] += 1
    return model


def edits1(word):
    """
    All edits that are one edit away from `word`.

    Credits : https://norvig.com/spell-correct.html
    Search up online for the algorithm as I believe part of working
    as a data scientist includes searching for the web like google
    and stackoverflow for answers when stuck.

    Args:
        word:   (str) word to be searched for
    Returns:
        set<str>
        Set of possible words after doing the delete,transpose,replace and insert op.
    """
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts = [a + c + b for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(corpus, word):
    """
    All edits that are two edits away from `word`.

    Credits : https://norvig.com/spell-correct.html
    Search up online for the algorithm as I believe part of working
    as a data scientist includes searching for the web like google
    and stackoverflow for answers when stuck.

    Args:
        corpus:  (defaultdictionary<str,int>) default dict of word and its freq
        word:   (str) word to be searched for
    Returns:
        set<str>
        Set of possible words after doing the delete,transpose,replace and insert op.
    """
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in corpus)


def known(corpus, _words):
    """
    The subset of `words` that appear in the dictionary of WORDS.

    Credits : https://norvig.com/spell-correct.html
    Search up online for the algorithm as I believe part of working
    as a data scientist includes searching for the web like google
    and stackoverflow for answers when stuck.

    Args:
        corpus:  (defaultdictionary<str,int>) default dict of word and its freq
        _words:   str) word to be searched for
    Returns:
        set<str>
        The subset of `words` that appear in the dictionary of corpus.
    """
    return set(w for w in _words if w in corpus)


def correct(corpus, word):
    """
    Function to retrieve the correct word according to a few level of checks
    starting from the best-case scenario

    Credits : https://norvig.com/spell-correct.html
    Search up online for the algorithm as I believe part of working
    as a data scientist includes searching for the web like google
    and stackoverflow for answers when stuck.

    Args:
        corpus:  (defaultdictionary<str,int>) default dict of word and its freq
        word:   (str) word to be searched for
    Returns:
        (str)
        Most probable spelling correction for word.
    """
    candidates = known(corpus, [word]) or known(corpus, edits1(word)) or known_edits2(corpus, word) or [word]
    return max(candidates, key=corpus.get)


def cli_helper():
    """
    Function prompt the user on how to use the spellchecker script

    Args:

    Returns:

    """
    print 'Usage:\tpython spellchecker.py [any_words]*'
    sys.exit(1)


if __name__ == "__main__":
    corpus_dict = get_freq()
    args = sys.argv[1:]
    if not args:
        cli_helper()
    for arg in args:
        regex_word = words(arg)
        if not regex_word:
            continue
        print correct(corpus_dict, regex_word[0])
        # import pdb
        # pdb.set_trace()

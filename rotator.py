def word_rotator_core(string_in=""):
    """
    This method rotate a letters in a words in a sentence
    :param string_in:
    :return: string_out or False
    """
    if type(string_in) is not str:                                                  # protection for a wrong input
        return False

    words_list = string_in.split(" ")                                               # Prepare data
    words_rev_list = []
    _tmp = ""

    for word in words_list:                                                         # Letters parsing
        word_l = list(word)
        word_l.reverse()                                                            # The core of rotation algorithm
        word_r = ""
        for _l in range(len(word_l)):
            if (word_l[_l] == ".") or (word_l[_l] == "!") or (word_l[_l] == "?"):   # Mark remove
                _tmp = word_l[_l]
            else:
                word_r += word_l[_l]
        words_rev_list.append(word_r.lower())                                       # Build final list

    string_out = ""
    for word_rl in range(len(words_rev_list)):
        string_out += words_rev_list[word_rl] + " "                                 # Building output string

    string_out = (string_out[0: -1]).capitalize() + _tmp                            # Prepare output string
    return string_out

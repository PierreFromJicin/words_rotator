def word_rotator_core(string_in=""):
    """
    This method rotate a letters in a words in a sentence
    :param string_in:
    :return: string_out or False
    """
    if type(string_in) is not str:                                                  # protection for a wrong input
        return False

    words_list = string_in.split(" ")                                               # data preparing
    words_rev_list = []
    _tmp = ""

    for word in words_list:                                 # parsing of letters
        word_l = list(word)
        word_l.reverse()                                    # the core of rotation algorithm
        word_r = ""
        for _l in range(len(word_l)):
            if word_l[_l] in ".!?":                         # removing of end mark
                _tmp = word_l[_l]
            else:
                word_r += word_l[_l]
        words_rev_list.append(word_r.lower())               # finalize list of words

    string_out = ""
    for word_rl in range(len(words_rev_list)):
        string_out += words_rev_list[word_rl] + " "         # make output string

    string_out = (string_out[0: -1]).capitalize() + _tmp    # prepare output string
    return string_out

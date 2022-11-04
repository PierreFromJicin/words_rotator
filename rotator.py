def word_rotator_core(string_in=""):
    """
    This method rotate a letters in a words in a sentence
    :param string_in:
    :return: string_out or False
    """
    if type(string_in) is not str:                          # protection for a wrong input
        return False

    words_list = string_in.split(" ")                               # data preparing
    words_rev_list: list = []
    _tmp: str = ""
    _commas: list = []
    _capital: list = []
    _comma_flag: bool = False
    _capital_flag: bool = False

    for word in words_list:                                         # parsing of letters
        word_l = list(word)
        word_l.reverse()                                            # the core of rotation algorithm
        word_r = ""
        for _l in range(len(word_l)):
            if word_l[_l] in ".!?":                                 # removing of end mark
                _tmp = word_l[_l]
            elif word_l[_l] == ",":                                 # commas detector
                _comma_flag = True
            elif word_l[_l].isupper:()                              # capital letter detector
                _capital_flag: = True
                word_r += word_l[_l]
            else:
                word_r += word_l[_l]
        if _comma_flag is True:                                     # commas stack
            _commas.append(1)
            _comma_flag = False
        elif _capital_flag is True:                                 # capital stack
            _capital.append(1)
            _capital_flag = False
        else:
            _commas.append(0)
            _capital.append(0)
        words_rev_list.append(word_r.lower())                       # finalize list of words

    string_out = ""
    for word_rl in range(len(words_rev_list)):                      # prepare output string
        if (_commas[word_rl] == 1) or (_capital[word_rl] == 1):
            if _commas[word_rl] == 1:
                string_out += words_rev_list[word_rl] + ", "
                if _capital[word_rl] == 1:
                words_rev_list[word_rl][0].upper()                  # <--- try use to .capitalize()
                # string_out += words_rev_list[word_rl] + " "
                else:
                    continue
            else:
                words_rev_list[word_rl].capitalize()
                string_out += words_rev_list[word_rl] + " "
        else:
            string_out += words_rev_list[word_rl] + " "

    string_out = (string_out[0: -1]).capitalize() + _tmp
    return string_out

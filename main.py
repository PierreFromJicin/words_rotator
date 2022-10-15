def word_rotator_core(string_in=""):
    if type(string_in) is not str:
        return False
    words_rev_list = []
    words_list = string_in.split(" ")
    number_of_words = len(words_list)
    print(f"word_list: {words_list} \nnumber_of_words: {number_of_words}")
    for word in words_list:
        print(word)
        word_l = list(word)
        print(word_l)
        word_l.reverse()
        print(word_l)
        word_r = ""
        for _l in range(len(word_l)):
            if word_l[_l] != ".":
                word_r += word_l[_l]
            print(word_r)
        words_rev_list.append(word_r.lower())
    string_out = ""
    for word_rl in range(len(words_rev_list)):
        string_out += words_rev_list[word_rl] + " "
    string_out = (string_out[0: -2] + ".").capitalize()
    return string_out


print(word_rotator_core("This is the testing sentence."))


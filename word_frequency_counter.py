def word_frequency_counter(words):
    diction = {}
    words_arr = words.split()
    for word_found in words_arr:
        diction[word_found] = diction.get(word_found, 0) + 1
    return diction

w = input("Give us some words?")
w = w.lower()
lorem_diction = word_frequency_counter(w)
print(lorem_diction)
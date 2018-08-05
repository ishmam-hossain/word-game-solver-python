import itertools
import enchant


def get_all_valid_words(word, size):
    dictionary = enchant.Dict("en_US")
    list_of_chars = list(word)

    all_combo = list(itertools.product(list_of_chars, repeat=size))
    unq_words = set()

    for combo in all_combo:
        wrd = ''.join(combo)
        if dictionary.check(wrd):
            unq_words.add(wrd)

    print(' '.join(unq_words))


if __name__ == '__main__':
    all_chars = input("Characters to make word with: ")
    desired_word_length = int(input("Desired word length: "))

    get_all_valid_words(all_chars, desired_word_length)

def is_one_char_phrase(phrase):
    word_list = phrase.split()
    word = "".join(word_list)

    if len(word_list) == len(word):
        return True

    return False


def optimize_n(n):
    if n < 10:
        return n - 3
    elif n < 15:
        return n
    else:
        return n - 2


def bucketize(phrase, n):
    if is_one_char_phrase(phrase):
        print(phrase.split())
    else:
        word_list = phrase.split()

        optimized_n = optimize_n(n)

        words_bucket = []
        temp = []
        counter = optimized_n
        for word in word_list:
            if counter > 0:
                temp.append(word + " ")
                counter -= len(word) + 1
            else:
                words_bucket.append(" ".join(temp).rstrip())
                temp.clear()
                counter += optimized_n

                temp.append(word + " ")
                counter -= len(word) + 1

        words_bucket.append(" ".join(temp).rstrip())

        print(words_bucket)


if __name__ == '__main__':
    bucketize("she sells sea shells by the sea", 10)
    bucketize("the mouse jumped over the cheese", 7)
    bucketize("fairy dust coated the air", 20)
    bucketize("a b c d e", 2)

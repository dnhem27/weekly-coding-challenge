
def lcs(word1, word2):
    # create empty matrix
    lengths_matrix = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for word1_index, word1_char in enumerate(word1):
        for word2_index, word2_char in enumerate(word2):
            if word1_char == word2_char:
                lengths_matrix[word1_index + 1][word2_index + 1] = lengths_matrix[word1_index][word2_index] + 1
            else:
                lengths_matrix[word1_index + 1][word2_index + 1] = max(lengths_matrix[word1_index + 1][word2_index],
                                                                       lengths_matrix[word1_index][word2_index + 1])

    # get substring from matrix
    longest_substring = ''
    index2 = len(word2)
    for index1 in range(1, len(word1) + 1):
        if lengths_matrix[index1][index2] != lengths_matrix[index1 - 1][index2]:
            longest_substring += word1[index1 - 1]

    return len(longest_substring)


if __name__ == '__main__':
    string1 = 'Minneapolis'
    string2 = 'Minnesota'

    answer = lcs(string1, string2)

    print(answer)
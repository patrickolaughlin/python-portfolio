# word_frequency.py
"""This program analyses the frequency of words in a file and
    prints a report of the most frequent words and their word
    count.
"""

# exclude special characters and numbers
PATTERN = '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~0123456789'


def by_frequency(pair):
    return pair[1]


def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report of the most frequent words.\n")

    while True:
        # get the sequence of words from the file
        filename = input("File to analyze('q' to quit)->  ")
        if filename == 'q':
            exit()
        try:
            file = open(filename, 'r')
            text = file.read()
            file.close()
            text = text.lower()
            break
        except IOError:
            print('Cannot open filename: %s' %filename)
            
    # remove special characters 
    for character in PATTERN:
        text = text.replace(character, ' ')
    words = text.split()

    # construct a dictionary of word counts
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # output analysis of n most frequent words.
    number_of_words = eval(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=by_frequency, reverse=True)
    for i in range(number_of_words):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))


if __name__ == '__main__':
    main()

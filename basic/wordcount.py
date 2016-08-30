#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import string


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def read_file(filename):

    with open(filename) as f:
        words = f.read();

    for c in string.punctuation:
        words = words.replace(c,' ')

    words = words.lower()
    words = words.split()

    dict = {}
    for key in words:
        if not key in dict.keys():
            dict[key] = 1
        else:
            dict[key] += 1
    return dict


def print_words(filename):
    count = read_file(filename)

    keys = list(count.keys())
    keys.sort()

    for item in keys:
        print('%s %s' % (item, count[item]))

def print_top(filename):
    count = read_file(filename)

    dict_invertido = {}
    for item in count:
        dict_invertido[count[item]] = item
    # organizes the output
    keys = list(dict_invertido.keys())
    keys.sort()
    keys.reverse()

    # prints the output
    for item in keys:
        print('%s %s' % (dict_invertido[item],item))

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()

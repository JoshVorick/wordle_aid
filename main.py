import csv
import math

words = {}
r1_words = []

with open('unigram_freq.csv', newline='') as csvfile:
    for row in csv.reader(csvfile):
        if len(row[0]) == 5 and int(row[1]) > 99999:
            words[row[0]] = int(row[1])
            r1_words.append(row[0])

print(len(words.keys()))


def matches_clue(word, w1, a1):
    for i in range(5):
        if a1[i] == 'x':
            if w1[i] in word:
                return False
        elif a1[i] == 'g':
            if w1[i] != word[i]:
                return False
        elif a1[i] == 'y':
            # TODO: double letter logic
            if w1[i] == word[i] or w1[i] not in word:
                return False
    return True

def calc_letter_freq(word_list):
    freqs = {}
    for w in word_list:
        for l in w:
            freq = math.log(words[w])
            if l not in freqs:
                freqs[l] = freq
            else:
                freqs[l] += freq

    return freqs

def print_word_freqs(freqs):
    for k in sorted(freqs, key = lambda x: -words[x]):
        print(k, ' :: ', words[k])

def print_letter_freqs(freqs):
    for k, v in sorted(freqs.items(), key = lambda x: -x[1]):
        print(k, ' :: ', v)


w1 = 'stale'
a1 = 'xyxxg'

r2_words = list(filter(lambda x: matches_clue(x, w1, a1), r1_words))

print(len(r1_words))
print(len(r2_words))

print(r2_words)
print()
print_word_freqs(r2_words)
print()
r2_freqs = calc_letter_freq(r2_words)
print_letter_freqs(r2_freqs)
print()

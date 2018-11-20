# -*- coding: utf-8 -*-
# coding: utf8
import math
import nltk
from nltk import SnowballStemmer

bare_txt = ""
stop_words = nltk.corpus.stopwords.words('english')
stop_symbols = '.,!?:;"-\n\r()'


def reader(bare_txt):
    stemmer = SnowballStemmer('english')
    stem_txt = ([stemmer.stem(x) for x in [y.strip(stop_symbols) for y in bare_txt.lower().split()] if x and (x not in stop_words)])

    first_dict = dict([])
    for word in stem_txt:
        if word in first_dict:
            first_dict[word] += 1
        else:
            first_dict[word] = 1

    second_dict = dict([])
    for key in first_dict.keys():
        second_dict[key] = first_dict[key]/len(stem_txt)*100

    return second_dict


def valualisation():
    a_K = 0 #балл за автора К
    a_N = 0 #балл за автора N

    txtN = open("file1.txt").read()
    txtN = txtN.decode('utf8')
    txtK = open("file2.txt").read()
    txtK = txtK.decode('utf8')
    txtS = open("file3.txt").read()
    txtS = txtS.decode('utf8')

    n_a_dict = reader(txtN)
    k_a_dict = reader(txtK)

    t_dict = reader(txtS)

    x = 0 #частота в % употр слова в А-тексте

    z = 0 #частота в % употр слова у K-автора
    y = 0 #частота в % употр слова у N-автора

    for word in t_dict.keys():
        x = t_dict[word]

        if word in n_a_dict.keys():
            y = n_a_dict[word]
        else:
            y = 0
        if word in k_a_dict.keys():
            z = k_a_dict[word]
        else:
            z = 0

        if math.fabs(y-x) > math.fabs(z-x):
            a_K += 1
        elif math.fabs(y-x) < math.fabs(z-x):
            a_N += 1

    np = a_N/len(t_dict)
    kp = a_K/len(t_dict)
    return "Probability for Author N =" + np+";\nProbability for Author K =" +kp

valualisation()
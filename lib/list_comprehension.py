#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for i in num_list:
        if i % 2 == 0:
            evens.append(i)
    return evens

def make_exclamation(sentence_list):
    exclamation = []
    for i in sentence_list:
        exclamation.append( i + "!")
    return exclamation
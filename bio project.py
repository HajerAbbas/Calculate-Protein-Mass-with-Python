# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 00:58:05 2020

@author: Acer
"""
prot = input('Enter protein sequence:')
mss = {
    'G': 57.02146,
    'A': 71.03711,
    'S': 87.03203,
    'P': 97.05276,
    'V': 99.06841,
    'T': 101.04768,
    'C': 103.00919,
    'L': 113.08406,
    'I': 113.08406,
    'N': 114.04293,
    'D': 115.02694,
    'Q': 128.05858,
    'K': 128.09496,
    'E': 129.04259,
    'M': 131.04049,
    'H': 137.05891,
    'F': 147.06841,
    'U': 150.95364,
    'R': 156.10111,
    'Y': 163.06333,
    'W': 186.07931,
    'O': 237.14773,
}
def calculate(mass):
    final = 0
    mass = list(mass)
    for i in mass:
        amount = mss.get(i)
        final += amount
    return final
print(calculate(prot))




wor = [1,2,2,2,5,4]
wo = 2

def main(word_list, word):
    for item in word_list:   
    	if(item==word):
	     	word_list.remove(word)
    re = word_list
    return re

print(main(wor, wo))









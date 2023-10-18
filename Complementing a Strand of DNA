'''The Secondary and Tertiary Structures of DNA
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s.
 '''

def complement(s):
    #associate key to value, this allows the for loop to run once using a dictionary, not replacing the same bp you already replaced previously
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sc = ""

    for bp in s[::-1]:
        sc+= complement_dict[bp]
    print(sc)

complement(s)

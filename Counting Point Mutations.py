'''
Problem

Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s
 and t
 of equal length, the Hamming distance between s
 and t
, denoted dH(s,t)
, is the number of corresponding symbols that differ in s
 and t
. See Figure 2.

Given: Two DNA strings s
 and t
 of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''

def difference(sequence):
    sequences = sequence.splitlines()
    seq1 = sequences[0]
    seq2 = sequences[1]
    
    differing_bases = [base1 for base1, base2 in zip(seq1, seq2) if base1 != base2]
    differing_bases += seq2[len(seq1):]  # Append the remaining characters from seq2 (if its length is larger than seq1)

    unmatched = ''.join(differing_bases)
    print(len(unmatched))

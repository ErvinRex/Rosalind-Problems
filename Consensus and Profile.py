# Consensus and Profile
# =====================
# 
# A matrix is a rectangular table of values divided into rows and columns. An
# m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to
# indicate the value found at the intersection of row i and column j. You may
# choose to think of A as a collection of m arrays, each of length n.
# 
# Say that we have a collection of DNA strings, all having the same length n.
# Their profile matrix is a 4×n matrix P in which P1,j represents the number of
# times that 'A' occurs in the jth position of one of the strings, P2,j
# represents the number of times that C occurs in the jth position, and so on
# (see below).
# 
# A consensus string c is a string of length n formed from our collection by
# taking the most common symbol at each position; the jth symbol of c therefore
# corresponds to the symbol having the maximum value in the j-th column of the
# profile matrix. Of course, there may be more than one most common symbol,
# leading to multiple possible consensus strings.
# 
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp).
# 
# Return: A consensus string and profile matrix for the collection. (If several
# possible consensus strings exist, then you may return any one of them.)
# 
# Sample Dataset
# --------------
# ATCCAGCT
# GGGCAACT
# ATGGATCT
# AAGCAACC
# TTGGAACT
# ATGCCATT
# ATGGCACT
# 
# Sample Output
# -------------
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6


from collections import defaultdict

def consensus_and_profile(input_str):
    # Split the input string into DNA strings&RosalindID using newline characters
    lines = input_str.strip().split('\n')

    # Separate the description lines (starting with '>') from the DNA strings, to remove Rosalind ID
    dna_strings = [line for line in lines if not line.startswith('>')]


    # Initialize the profile matrix dictionary
    profile_matrix = defaultdict(list)
    #get the length of the sequences (all are assumed to be the same)
    n = len(dna_strings[0])

    # Iterate through the characters to get a count for the bases at each position
    for j in range(n):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for dna in dna_strings:
            counts[dna[j]] += 1
        #add the base and count of the base at each position into the profile matrix
        for base, count in counts.items():
            profile_matrix[base].append(count)

    # Find the consensus string
    #list comprehension to iterate through each position in the profile matrix
    #lambda function is our key, specifies that i want the base and j (think of it like the index of each position) in the range of the sequence 
    consensus = ''.join(max(profile_matrix, key=lambda base: profile_matrix[base][j]) for j in range(n))

    return {
        'consensus': consensus,
        'profile_matrix': dict(profile_matrix)
    }

result = consensus_and_profile(input_str)

# Print the consensus string
print(result['consensus'])

# Print the profile matrix
for base, counts in result['profile_matrix'].items():
    print(f"{base}: {' '.join(map(str, counts))}")

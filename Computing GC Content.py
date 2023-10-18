'''
Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

def GCcontent(FASTA):
    dictionary = {}
    header = None # To keep track of the current sequence header
    for line in FASTA.split('\n'):
        if line.startswith('>'):
            header = line[1:]  #Extract the header (excluding '>') as the key
            dictionary[header] = 0 # Initialise the key in the dictionary
        else:
            seq = line.strip()
            count_g = seq.count('G')
            count_c = seq.count('C')
            gc = count_g + count_c
            gcpercent = (gc/len(seq)) * 100
            dictionary[header] += gcpercent # Add the GC percentage to the current header
    largest_key = max(dictionary, key=dictionary.get)
    largest_value = round(dictionary[largest_key], 3)
    print(largest_key,"\n",largest_value)

'''
Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s
 corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
'''
def translate(RNAseq):
    #codon to amino acid mapping
    codon_table = {
        "UUU" : "F", "CUU" : "L", "AUU" : "I",
        "GUU" : "V", "UUC" : "F", "CUC": "L",
        "AUC" : "I", "GUC" : "V", "UUA" : "L",
        "CUA" : "L", "AUA" : "I", "GUA" : "V",
        "UUG" : "L", "CUG" : "L", "AUG" : "M",
        "GUG" : "V", "UCU" : "S", "CCU" : "P",
        "ACU" : "T", "GCU" : "A", "UCC" : "S",
        "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S", "CCA" : "P", "ACA" : "T",
        "GCA" : "A", "UCG" : "S", "CCG" : "P",
        "ACG" : "T", "GCG" : "A", "UAU" : "Y",
        "CAU" : "H", "AAU" : "N", "GAU" : "D",
        "UAC" : "Y", "CAC" : "H", "AAC" : "N",
        "GAC" : "D", "UAA" : "Stop", "CAA" : "Q", "AAA" : "K",     
        "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K",
        "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S",    
        "GGU" : "G", "UGC" : "C", "CGC" : "R",
        "AGC" : "S", "GGC" : "G", "UGA" : "Stop", "CGA" : "R",
        "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R",
        "AGG" : "R", "GGG" : "G",
        }
    #Initiation of empty string - where the final sequence is outputted
    translation = ""
    #set position at the beginning (so we can move across)
    pos = 0
    #for 3 strings in the string (sequence), matching with the codon table
    while RNAseq[pos:pos+3] in codon_table:
        #create a variable that takes the string matching the amino acid in codon table
        amino_acid = codon_table[RNAseq[pos:pos+3]]
        #if a stop codon is seen, remove it from the sequence
        if amino_acid != "Stop":
            #remaining sequence put into "translation" string
            translation += amino_acid
            #move across by 3 and restart the loop
        pos+=3    
    print(translation)

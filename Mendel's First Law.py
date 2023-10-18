'''
Problem

For example, say that we have a bag containing 3 red balls and 2 blue balls. If we let X
 represent the random variable corresponding to the color of a drawn ball, then the probability of each of the two outcomes is given by Pr(X=red)=35
 and Pr(X=blue)=25
.

Random variables can be combined to yield new random variables. Returning to the ball example, let Y
 model the color of a second ball drawn from the bag (without replacing the first ball). The probability of Y
 being red depends on whether the first ball was red or blue. To represent all outcomes of X
 and Y
, we therefore use a probability tree diagram. This branching diagram represents all possible individual probabilities for X
 and Y
, with outcomes at the endpoints ("leaves") of the tree. The probability of any outcome is given by the product of probabilities along the path from the beginning of the tree; see Figure 2 for an illustrative example.

An event is simply a collection of outcomes. Because outcomes are distinct, the probability of an event can be written as the sum of the probabilities of its constituent outcomes. For our colored ball example, let A
 be the event "Y
 is blue." Pr(A)
 is equal to the sum of the probabilities of two different outcomes: Pr(X=blue and Y=blue)+Pr(X=red and Y=blue)
, or 310+110=25
 (see Figure 2 above).

Given: Three positive integers k
, m
, and n
, representing a population containing k+m+n
 organisms: k
 individuals are homozygous dominant for a factor, m
 are heterozygous, and n
 are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''
def mendel(k, m, n):
    total_population = k + m + n
    
    # Calculate the probabilities of dominant allele combinations
    prob_kk = (k / total_population) * ((k - 1) / (total_population - 1))
    prob_km = (k / total_population) * (m / (total_population - 1))
    prob_kn = (k / total_population) * (n / (total_population - 1))
    prob_mk = (m / total_population) * (k / (total_population - 1))
    prob_mm = (m / total_population) * ((m - 1) / (total_population - 1)) * 0.75  # Heterozygous cross
    prob_mn = (m / total_population) * (n / (total_population - 1)) * 0.5       # Heterozygous cross
    prob_nk = (n / total_population) * (k / (total_population - 1))
    prob_nm = (n / total_population) * (m / (total_population - 1)) * 0.5       # Heterozygous cross
    
    # Sum up the probabilities of producing an offspring with a dominant allele
    total_prob_dominant = prob_kk + prob_km + prob_kn + prob_mk + prob_mm + prob_mn + prob_nk + prob_nm
    
    return total_prob_dominant

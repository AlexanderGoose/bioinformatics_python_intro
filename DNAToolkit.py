import collections
from utilities import *
from structures import *

#####################################################
#        Validating and counting nucleotides        # 
#####################################################

# ensure that the string is a valid dna sequence
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

# counts freq and returns dict
def countNucFrequency(dna_seq):
    freq_dict = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for nuc in dna_seq:
        freq_dict[nuc] += 1
    return freq_dict

# same as above but using collections method
def countNucFrequencyCollections(dna_seq):
    return dict(collections.Counter(dna_seq))


################################################
#      Transcription, Reverse Complement       # 
################################################

def transcription(dna_seq):
    """ DNA -> RNA """
    return dna_seq.replace('T', 'U')

def complement(dna_seq):
    return ''.join([dna_complement[nuc] for nuc in dna_seq])

def revererse_complement(dna_seq):
    """ Finds the complement for each nucleotide, then returns the reverse. """
    return ''.join([dna_complement[nuc] for nuc in dna_seq])[::-1]

def print_dna_plus_rev_comp(dna_seq):
    """ Prints out the seq paried with it's reverse complement """
    print("[5] DNA String + Complement")
    print(f"    5' {colored(dna_seq)} 3'")
    print(f"       {''.join(['|' for i in range(len(dna_seq))])}   ")
    print(f"    3' {colored(complement(dna_seq))} 5'")
    return "\n"



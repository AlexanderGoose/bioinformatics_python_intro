import collections
from utilities import *
from structures import *
from collections import Counter

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
    print("\n[5] DNA String + Complement")
    print(f"    5' {colored(dna_seq)} 3'")
    print(f"       {''.join(['|' for i in range(len(dna_seq))])}   ")
    print(f"    3' {colored(complement(dna_seq))} 5'")
    return ""


#####################################
#      GC Content Calcualtion       # 
#####################################

def gc_content(dna_seq):
    """ Returns the GC content of a given DNA/RNA sequence """
    return round((dna_seq.count('C') + dna_seq.count('G')) / len(dna_seq) * 100)

def gc_content_subsec(dna_seq, k=20):
    """ GC content in a DNA/RNA sub-sequence of length k. k set to 20 by default """
    res = []
    for i in range(0, len(dna_seq) - k + 1, k):
        subseq = dna_seq[i: i + k]
        res.append(gc_content(subseq))
    return res


#######################################
#      Translation, Codon Usage       # 
#######################################

def translate_seq(seq, init_pos=0):
    """ Translates a DNA sequence into an aminoacid sequence """
    # return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]
    acids = []
    for position in range(init_pos, len(seq) - 2, 3):  
        # find the key in the dict with the current set of 3          
        current_codon = (DNA_Codons[seq[position:position + 3]])
        acids.append(current_codon)

    return acids

def codon_usage(dna_seq, aminoacid):
    """ Provides the frequency of each codon encoding a given aminoacid in a DNA sequence """
    tmp_list = []
    for i in range(0, len(dna_seq) - 2, 3):
        if DNA_Codons[dna_seq[i: i + 3]] == aminoacid:
            tmp_list.append(dna_seq[i:i + 3])

    freq_dict = dict(Counter(tmp_list))
    total_wigth = sum(freq_dict.values())
    for dna_seq in freq_dict:
        freq_dict[dna_seq] = round(freq_dict[dna_seq] / total_wigth, 2)
    return freq_dict

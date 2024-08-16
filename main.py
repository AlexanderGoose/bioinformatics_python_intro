from DNAToolkit import *
import random
from utilities import *

# rnd_dna_str = 'ATGCGTAGATCGATCGAGGCTATACTTCTCA'

# we can use list comp to create a random dna seq
# each time the file is ran.
rnd_dna_str = ''.join([random.choice(nucleotides) for nuc in range(40)])

# print(validateSeq(rnd_dna_str))

DNA_Str = validateSeq(rnd_dna_str)
# print(countNucFrequency(DNA_Str))

print(f'\n[1] Sequence:               {colored(DNA_Str)}')
print(f'[2] Sequence Length:        {len(DNA_Str)}')
print(colored(f'[3] Sequence Frequency:     {countNucFrequency(DNA_Str)}'))
print(f'[4] Transcripted Sequence:  {transcription(DNA_Str)}')

print(f'{print_dna_plus_rev_comp(DNA_Str)}')

print(f'[6] {revererse_complement(DNA_Str)}')
from DNAToolkit import *
import random
from utilities import *

# we can use list comp to create a random dna seq
# each time the file is ran.
rnd_dna_str = ''.join([random.choice(nucleotides) for nuc in range(40)])

DNA_Str = validateSeq(rnd_dna_str)

print(f'\n[1] Sequence:               {colored(DNA_Str)}')

print(f'[2] Sequence Length:        {len(DNA_Str)}')

print(colored(f'[3] Sequence Frequency:     {countNucFrequency(DNA_Str)}'))

print(f'[4] Transcripted Sequence:  {colored(transcription(DNA_Str))}')

print(f'{print_dna_plus_rev_comp(DNA_Str)}')

print(f'[6] Reverse Complement: {colored(revererse_complement(DNA_Str))}')

print(f'[7] GC Content: {gc_content(DNA_Str)}%')

print(f'[8] GC Content in Subsection (k=5): {gc_content_subsec(DNA_Str, k=5)}')

print(f'[9] Aminoacids Sequence from DNA:\n    {translate_seq(DNA_Str)}')

print(f'[10] Codon Frequencies (L): {codon_usage(DNA_Str, "L")}')
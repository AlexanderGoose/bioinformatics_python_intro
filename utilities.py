def colored(dna_seq):
    COLORS = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m',
    }

    tmp_str = ''

    for nuc in dna_seq:
        if nuc in COLORS:
            tmp_str += COLORS[nuc] + nuc
        else:
            tmp_str += COLORS['reset'] + nuc

    return tmp_str + '\033[0;0m'
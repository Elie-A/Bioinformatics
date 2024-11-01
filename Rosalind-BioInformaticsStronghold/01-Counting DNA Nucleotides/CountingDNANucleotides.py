import collections

def countNucleotidesFrequency(dna_sequence):
    # freqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # for nucleotide in dna_sequence:
    #     freqDict[nucleotide] += 1
    # return freqDict
    return dict(collections.Counter(dna_sequence))
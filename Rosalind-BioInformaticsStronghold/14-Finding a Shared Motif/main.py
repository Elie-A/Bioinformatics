from FindingASharedMotif import *

def main():
    # Read the DNA strings from a FASTA file
    strings = []
    with open("Rosalind-BioInformaticsStronghold\\14-Finding a Shared Motif\\rosalind_lcsm.txt", "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            strings.append(str(record.seq))
    
    # Find and print the longest common substring
    result = longest_common_substring(strings)
    print(result)

# Run the main function
main()

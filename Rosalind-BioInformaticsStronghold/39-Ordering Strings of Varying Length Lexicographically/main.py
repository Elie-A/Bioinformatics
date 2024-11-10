from OrderingStringsOfVaryingLengthLexicographically import *

def main():
    filename = 'Rosalind-BioInformaticsStronghold\\39-Ordering Strings of Varying Length Lexicographically\\rosalind_lexv.txt'  # Replace with your actual file name
    alphabet, n = read_data_from_file(filename)
    
    # Generate strings
    strings = generate_strings(alphabet, n)
    
    # Sort strings lexicographically based on the given order of the alphabet
    strings.sort(key=lambda x: [alphabet.index(c) for c in x])
    
    # Output
    for s in strings:
        print(s)

if __name__ == "__main__":
    main()

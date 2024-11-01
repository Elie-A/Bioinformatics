def calculate_protein_mass(protein_string):
    # Define the monoisotopic mass table
    MONOISOTOPIC_MASS_TABLE = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
        'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276,  'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
        'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333
    }

    # Calculate the total weight of the protein string
    total_mass = sum(MONOISOTOPIC_MASS_TABLE[aa] for aa in protein_string)
    return total_mass

# Reading protein string from file and calculating weight
def calculate_weight_from_file(filename):
    # Read protein string from the input file
    with open(filename, 'r') as file:
        protein_string = file.readline().strip()
    
    # Calculate the protein mass
    total_mass = calculate_protein_mass(protein_string)
    
    # Print or return the total mass rounded to 3 decimal places
    print(f"{total_mass:.3f}")


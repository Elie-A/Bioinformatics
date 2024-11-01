from FindingAProteinMotif import *

def main(filename):
    uniprot_ids = read_uniprot_ids_from_file(filename)
    
    for uniprot_id in uniprot_ids:
        # Fetch the protein sequence
        sequence = fetch_protein_sequence(uniprot_id)
        if sequence is None:
            continue
        
        # Find the locations of the motif
        locations = find_motif_locations(sequence)
        
        # Output the results
        if locations:
            print(uniprot_id)
            print(' '.join(map(str, locations)))

# Specify the filename containing the UniProt IDs
filename = 'Rosalind-BioInformaticsStronghold\\16-Finding a Protein Motif\\rosalind_mprt.txt'
main(filename)

import requests
import re

def fetch_protein_sequence(uniprot_id):
    """
    Fetch the protein sequence from the UniProt database in FASTA format.
    """
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code == 200:
        # The response text will be in FASTA format
        lines = response.text.splitlines()
        # Skip the header line (first line) and join the rest as a single sequence
        sequence = ''.join(lines[1:])
        return sequence
    else:
        print(f"Failed to fetch data for ID: {uniprot_id}")
        return None

def find_motif_locations(sequence):
    """
    Find the locations of the N-glycosylation motif in the protein sequence.
    The motif is defined as N{P}[ST]{P}.
    """
    # Convert the motif regex into a format suitable for re
    motif_regex = re.compile(r'N[^P][ST][^P]')
    
    # Find all matches
    locations = []
    for match in motif_regex.finditer(sequence):
        # The start position is 1-based
        locations.append(match.start() + 1)
    
    return locations

def read_uniprot_ids_from_file(filename):
    """
    Read UniProt IDs from a specified file.
    Each ID should be on a new line.
    """
    with open(filename, 'r') as file:
        uniprot_ids = [line.strip() for line in file if line.strip()]
    return uniprot_ids
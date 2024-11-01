def find_substring_locations(s, t):
    """Find all starting positions of substring t in string s (1-based indexing)."""
    positions = []
    start = 0

    # Loop to find all occurrences of t in s
    while True:
        start = s.find(t, start)
        if start == -1:  # No more occurrences
            break
        # Add position with 1-based indexing
        positions.append(start + 1)
        start += 1  # Move start to the next position

    return positions

def read_data_from_file(file_path):
    """Read the strings s and t from a file."""
    with open(file_path, 'r') as file:
        s = file.readline().strip()  # First line is string s
        t = file.readline().strip()  # Second line is string t
    return s, t
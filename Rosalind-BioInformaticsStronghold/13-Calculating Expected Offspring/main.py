from CalculatingExpectedOffspring import *

def main():
    # Sample input, replace with reading from file if needed
    with open("Rosalind-BioInformaticsStronghold\\13-Calculating Expected Offspring\\rosalind_iev.txt", "r") as file:
        data = file.read().strip()
    couples = list(map(int, data.split()))
    
    # Calculate expected dominant offspring
    result = expected_dominant_offspring(couples)
    
    # Print the result rounded to one decimal place
    print(f"{result:.1f}")

# Run the main function
main()

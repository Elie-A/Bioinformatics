from IntroductionToRandomStrings import *

file_path = 'Rosalind-BioInformaticsStronghold\\28-Introduction to Random Strings\\rosalind_prob.txt'
result = read_data_and_calculate(file_path)

# Print the output as space-separated values, rounded to three decimal places
print(" ".join(f"{r:.3f}" for r in result))

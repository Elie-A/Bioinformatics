from EnumeratingOrientedGeneOrderings import *

with open("Rosalind-BioInformaticsStronghold\\29-Enumerating Oriented Gene Orderings\\rosalind_sign.txt", "r") as file:
    n = int(file.readline().strip())

count, signed_perms = signed_permutations(n)

# Output results
print(count)
for perm in signed_perms:
    print(" ".join(map(str, perm)))

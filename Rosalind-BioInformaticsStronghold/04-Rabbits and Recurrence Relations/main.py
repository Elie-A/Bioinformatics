from RabbitsAndReccurenceRelations import *

with open("Rosalind-BioInformaticsStronghold\\04-Rabbits and Recurrence Relations\\rosalind_fib.txt", "r") as file:
    n, k = map(int, file.read().strip().split())

# Calculate and display the total number of rabbit pairs
result = rabbit_pairs(n, k)
print(result)
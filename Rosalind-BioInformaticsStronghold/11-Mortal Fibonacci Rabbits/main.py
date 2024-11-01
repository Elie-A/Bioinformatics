from MortalFibonacciRabbits import *

# Read the dataset from file
with open("Rosalind-BioInformaticsStronghold\\11-Mortal Fibonacci Rabbits\\rosalind_fibd.txt", "r") as file:
    n, m = map(int, file.read().strip().split())

# Get the result and print it
result = mortal_fibonacci_rabbits(n, m)
print(result)

import matplotlib.pyplot as plt
import math

# Function to calculate the frequency of first 2 digits according to Benford's Law
def benfords_law():
    digits = range(10)
    freqs = [math.log10(1 + 1/d)*100 for d in digits]
    return freqs

# Create a bar chart of the first 2 digits according to Benford's Law
plt.bar(range(1, 10), benfords_law()[1:], align='center')
plt.xticks(range(1, 10))
plt.xlabel('First 2 digits')
plt.ylabel('Frequency (%)')
plt.title("Benford's Law first 2 digit chart")
plt.show()
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

def benford_law(x):
    # Define a function that returns the logarithm of 1 plus the inverse of a number.
    # This is the formula for Benford's Law.
    return np.log10(1 + 1/x)

def benford_law_first_two(x):
    # Define a function that calculates the sum of the logarithm of 1 plus the inverse of
    # a number for the first 10 numbers that start with a certain digit.
    # This is the formula for the distribution of the first two digits according to Benford's Law.
    return sum(math.log10(1+1/(10*i+x)) for i in range (1,10))

#data = pd.read_csv('products.3.csv', low_memory=False)
data = pd.read_csv('new.data.csv', low_memory=False)

# Extract the first digit of each payment amount in the dataset and store it in an array.
first_digits = np.array([int(str(num)[0]) for num in data['Total_Amount_of_Payment_USDollars']])
#first_digits = np.array([int(str(num)[0]) for num in data['Number']])
# Extract the first two digits of each payment amount that is greater than or equal to 10 and store it in an array.
first_two_digits = np.array([int(str(num)[0:2]) for num in data['Total_Amount_of_Payment_USDollars'] if num >= 10])
#first_two_digits = np.array([int(str(num)[0:2]) for num in data['Number'] if num >= 10])
# Print the first two digits array to check if it's being extracted correctly.
#print(first_two_digits)


# Calculate the number of times each digit appears as the first digit of a payment amount.
digit_counts = [np.sum(first_digits == digit) for digit in range(1, 10)]

# Calculate the number of times each two-digit combination appears as the first two digits of a payment amount.
first_two_digit_counts = [np.sum(first_two_digits == digit) for digit in range(10, 100)]


# Calculate the frequency of each digit appearing as the first digit of a payment amount.
digit_frequencies = digit_counts / np.sum(digit_counts)

# Calculate the frequency of each two-digit combination appearing as the first two digits of a payment amount.
first_two_digit_frequencies = first_two_digit_counts / np.sum(first_two_digit_counts)
#print (first_two_digit_counts)
#print(np.sum(first_two_digit_counts))
# Calculate the expected frequency of each digit appearing as the first digit of a payment amount according to Benford's Law.
expected_frequencies = benford_law(np.arange(1, 10))

# Calculate the expected frequency of each two-digit combination appearing as the first two digits of a payment amount according to Benford's Law.
expected_first_two_digit_frequencies = (np.array([np.sum([benford_law_first_two((10*i+j)) for i in range(10)]) for j in range(10, 100)]))
#print (expected_first_two_digit_frequencies)
# Calculate the absolute difference between the expected and observed frequency of each digit appearing as the first digit of a payment amount.
differences = [(i+1, abs(digit_frequencies[i] - expected_frequencies[i])) for i in range(9)]

# Sort the differences in descending order.
sorted_diff = sorted(differences, key=lambda x: x[1], reverse=True)

# Calculate the absolute difference between the expected and observed frequency of each two-digit combination appearing as the first two digits of a payment amount.
first_two_differences = [(i+10, abs(first_two_digit_frequencies[i] - expected_first_two_digit_frequencies[i])) for i in range(90)]

# Sort the differences in descending order.
sorted_first_two_diff = sorted(first_two_differences, key=lambda x: x[1], reverse=True)

print("Ranking of differences from highest to lowest for the first digit:")
for digit, diff in sorted_diff:
    print("Absolute difference for digit", digit, ":", diff)

print("\nRanking of differences from highest to lowest for the first two digits:")
for digit, diff in sorted_first_two_diff:
    print("Absolute difference for digit", digit, ":", diff)
#this section is all graphing 
plt.subplot(211)
plt.plot(np.arange(1, 10), expected_frequencies, 'bo-', label='Benford\'s Law')
plt.plot(np.arange(1, 10), digit_frequencies, 'ro-', label='Data First Digits')
plt.ylabel('Frequency (linear scale)')
plt.title('Benford\'s Law')
plt.legend()

plt.figure()
#plt.plot(range(10, 100), expected_first_two_digit_frequencies, 'bo-', label='Benford\'s Law 1st Two Digits')
plt.plot(range(10, 100), first_two_digit_frequencies, 'ro-', label='Data First Two Digits')
plt.xlabel('Digit')
plt.ylabel('Frequency (linear scale)')
plt.title('Benford\'s Law on First Two Digits')
plt.yscale('linear')
plt.legend()
plt.show()

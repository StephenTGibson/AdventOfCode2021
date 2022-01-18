# Import pandas to read csv
import pandas as pd
# Create dataframe from csv (contains 1 column only)
# Force string type to keep leading zeros
df = pd.read_csv('task3.csv', header=None, delimiter='\n', dtype = str)
# Create list containing each row entry
rowsList = [row[0] for row in df.to_numpy()]

# Print summary
print(f'Number of binary numbers: {len(rowsList)}')

# Initialise empty dictionary to hold counts
countDict = {}

# Iterate over binary numbers
for binaryNum in rowsList:
    # Iterate over characters in each binary number
    for i, char in enumerate(binaryNum):
        # Check if current index is not yet in dictionary (as key)
        if i not in countDict:
            # Check if current character is a 0
            if char == '0':
                # Initialise count at this index position
                # Number at index 0 refers to count of zeros
                # Number at index 1 refers to count of ones
                countDict[i] = [1,0]
            # Check if current character is a 1
            elif char == '1':
                # Initialise count at this index position
                countDict[i] = [0,1]
            # Check for unexpected input
            else:
                print(f'Something else happened: {char}')
        # If current index already in dictionary (as key)
        else:
            # Check if current character is a 0
            if char == '0':
                # Increment count of zeros
                countDict[i][0] += 1
            # Check if current character is a 1
            elif char == '1':
                # Increment count of ones
                countDict[i][1] += 1

# Initialise empty strings to hold binary numbers
gammaBinary = ''
epsilonBinary = ''

# Iterate over keys in dictionary of counts
for binaryIdx in countDict:
    # Check if count of zeros greater than count of ones
    if countDict[binaryIdx][0] > countDict[binaryIdx][1]:
        # Concatenate 0 and 1 respectively to binary number strings
        gammaBinary += '0'
        epsilonBinary += '1'
    # Check if count of zeros less than count of ones
    elif countDict[binaryIdx][0] < countDict[binaryIdx][1]:
        # Concatenate 1 and 0 respectively to binary number strings
        gammaBinary += '1'
        epsilonBinary += '0'
    # Check for (unexpected) equal counts of zeros and ones
    else:
        print('Equal count of 0s and 1s')

# Helper function to calculate decimal value from binary
def decFromBinary(binaryStr):
    # Initialise decimal integer
    decimalInt = 0
    # Iterate over indices of characters in binary number
    for binaryIdx in range(len(binaryStr)):
        # Increase decimal value by value dependent on current index
        decimalInt += 2**(len(binaryStr)-(binaryIdx+1)) * \
            int(binaryStr[binaryIdx])
    # Return decimal value
    return decimalInt

# Calculate decimal numbers from binary
gammaDec = decFromBinary(gammaBinary)
epsilonDec = decFromBinary(epsilonBinary)

# Print results
print(f'gammaBinary: {gammaBinary}')
print(f'epsilonBinary: {epsilonBinary}')

print(f'gammaDec: {gammaDec}')
print(f'epsilonDec: {epsilonDec}')

print(f'power consumption = product: {gammaDec * epsilonDec}')

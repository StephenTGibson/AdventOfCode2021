# Import pandas to read csv
import pandas as pd
# Create dataframe from csv (contains 1 column only)
# Force string type to keep leading zeros
df = pd.read_csv('task3.csv', header=None, delimiter='\n', dtype = str)
# Create list containing each row entry
rowsList = [row[0] for row in df.to_numpy()]

# Print summary
print(f'Number of binary numbers: {len(rowsList)}')

# Helper function to count number of zeros or ones
# at pos for all strings in listBinary
def countPos(binaryList, pos):
    # Initialise counts
    zeros = 0
    ones = 0
    # Iterate over binary numbers in list
    for binaryNum in binaryList:
        # Check if character at pos is a 0
        if binaryNum[pos] == '0':
            # Increment zeros count
            zeros += 1
        # Check if character at pos is a 1
        elif binaryNum[pos] == '1':
            # Increment ones count
            ones += 1
        # Check for unexpected input
        else:
            print(f'Something else happened: {binaryNum[pos]}')
    # Return counts
    return zeros, ones


# Function to calculate oxygen binary number
def oxyGen(binaryList):
    # Create copy of input list of binary numbers (to make changes)
    binaryListOxy = binaryList.copy()
    # Initialise variable to track current position within binary numbers
    pos = 0
    # Loop until only 1 number is remaining in copied list of binary numbers
    while len(binaryListOxy) > 1:
        # Calculate count of zeros and ones at pos in all remaining numbers
        zeros, ones = countPos(binaryListOxy, pos)
        # Check if there are more zeros than ones
        if zeros > ones:
            # Identify most common digit as a zero
            mostCommon = '0'
        # Otherwise there are more ones than zeros or equal
        else:
            # Identify most common digit as a one
            mostCommon = '1'
        # Create new list of binary numbers from previous list
        # Exclude any numbers where digit at pos is not equal to mostCommon
        binaryListOxy = [binStr for binStr in binaryListOxy if \
            binStr[pos] == mostCommon]
        # Increment pos (move along one position in binary numbers)
        pos += 1
    # Return only remaining binary number
    return binaryListOxy[0]


# Function to calculate co2 binary number
# Same functionality as oxyGen() except uses least common
# instead of most common logic to exclude binary numbers
def co2scrub(binaryList):
    # Create copy of input list of binary numbers (to make changes)
    binaryListCo2 = binaryList.copy()
    # Initialise variable to track current position within binary numbers
    pos = 0
    # Loop until only 1 number is remaining in copied list of binary numbers
    while len(binaryListCo2) > 1:
        # Calculate count of zeros and ones at pos in all remaining numbers
        zeros, ones = countPos(binaryListCo2, pos)
        # Check if there are more zeros than ones
        if zeros > ones:
            # Identify least common digit as a one
            leastCommon = '1'
        # Otherwise there are more ones than zeros or equal
        else:
            # Identify least common digit as a zero
            leastCommon = '0'
        # Create new list of binary numbers from previous list
        # Exclude any numbers where digit at pos is not equal to leastCommon
        binaryListCo2 = [binStr for binStr in binaryListCo2 if \
            binStr[pos] == leastCommon]
        # Increment pos (move along one position in binary numbers)
        pos += 1
    # Return only remaining binary number
    return binaryListCo2[0]


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


# Calculate oxygen and co2 binary numbers
oxyBin = oxyGen(rowsList)
co2Bin = co2scrub(rowsList)

# Calculate decimal numbers from binary
oxyDec = decFromBinary(oxyBin)
co2Dec = decFromBinary(co2Bin)

# Print results
print(f'oxygen binary: {oxyBin}')
print(f'co2 binary: {co2Bin}')

print(f'oxygen decimal: {oxyDec}')
print(f'co2 decimal: {co2Dec}')

print(f'life support rating = product: {oxyDec * co2Dec}')

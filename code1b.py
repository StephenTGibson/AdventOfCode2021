# Import pandas to read csv
import pandas as pd
# Create dataframe from csv (contains 1 column only)
df = pd.read_csv('task1.csv', header=None, delimiter='\n')
# Create list containing each row entry
rowsList = [row[0] for row in df.to_numpy()]

# Print summary
print(f'Number of depths: {len(rowsList)}')

# Size of moving window of depths
windowSize = 3

# Initialise list of summed window depths
# First summed depth is sum of first 3 depths
listWindowDepths = [sum(rowsList[:3])]

# Iterate over depth indices
# Skip first indices - start from 2nd complete window
for i in range(windowSize, len((rowsList))):
    # Append current window depth sum to list
    # Sum equals previous sum - the earliest depth added + the current depth
    listWindowDepths.append(listWindowDepths[-1] - rowsList[i-3] + rowsList[i])

# Initialise counter
counter = 0

# Iterate over depth indices
# Skip first index (cannot compare it to previous)
for i in range(1, len(listWindowDepths)):
    # Check if current depth greater than previous
    if listWindowDepths[i] > listWindowDepths[i-1]:
        # Increment counter
        counter += 1

print(counter)

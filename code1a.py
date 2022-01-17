# Import pandas to read csv
import pandas as pd
# Create dataframe from csv (contains 1 column only)
df = pd.read_csv('task1.csv', header=None, delimiter='\n')
# Create list containing each row entry
rowsList = [row[0] for row in df.to_numpy()]

# Print summary
print(f'Number of depths: {len(rowsList)}')

# Initialise counter
count = 0

# Iterate over depth indices
# Skip first index (cannot compare it to previous)
for i in range(1, len(rowsList)):
    # Check if current depth greater than previous
    if rowsList[i] > rowsList[i-1]:
            # Increment count
            counter += 1

print(count)

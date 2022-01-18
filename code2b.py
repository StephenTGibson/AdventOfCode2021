# Import pandas to read csv
import pandas as pd
# Create dataframe from csv (contains 1 column only)
df = pd.read_csv('task2.csv', header=None, delimiter='\n')
# Create list containing each row entry
rowsList = [row[0] for row in df.to_numpy()]

# Print summary
print(f'Number of instructions: {len(rowsList)}')

# Initialise variables
depth = 0
forward = 0
aim = 0

# Iterate over instructions
for instruct in rowsList:
    # Check first character of instruction (f = forward)
    if instruct[0] == 'f':
        # Increase forward by amount (last character of instruction string)
        # Increase depth by product of aim and amount
        forward += int(instruct[-1])
        depth += aim * int(instruct[-1])
    # Check first character of instruction (d = down)
    elif instruct[0] == 'd':
        # Increase aim by amount
        aim += int(instruct[-1])
    # Check first character of instruction (u = up)
    elif instruct[0] == 'u':
        # Decrease aim by amount
        aim -= int(instruct[-1])
    # Check for unexpected input
    else:
        print(f'Something else happened:: {instruct}')

# Print results
print(f'depth: {depth}')
print(f'forward: {forward}')
print(f'product: {depth * forward}')

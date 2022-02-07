# Import csv to read input
import csv

# Open input csv
with open('task5.csv') as csv_file:
    # Use the spaces to split each line
    csv_reader = csv.reader(csv_file, delimiter=' ')
    # Initialise empty list to store vent coordinates
    hydroVentsList = []
    # Iterate over each vent (row)
    for row in csv_reader:
        # Extract coordinates from each line
        x1, y1 = row[0].split(',')
        x2, y2 = row[2].split(',')
        # Append coordinates to list in the form: ((x1, y1), (x2, y2))
        hydroVentsList.append([(int(x1), int(y1)), (int(x2), int(y2))])
    # Print summary
    print(f'Count of hydro vents: {len(hydroVentsList)}')

# Function to determine if a vent has a diagonal path
def checkVentDiag(vent):
    # Check if both x1 and x2 are not equal and y1 and y2 are also not equal
    if vent[0][0] != vent[1][0] and vent[0][1] != vent[1][1]:
        # This will indicate vent is diagonal
        return True
    # Otherwise vent will be either horizontal or vertical
    else:
        return False

# Initialise empty lists to hold diagonal and non-diagonal vents
diagVentsList = []
notDiagVentsList = []

# Iterate over vents in list
for vent in hydroVentsList:
    # Check if vent is diagonal
    if checkVentDiag(vent):
        # Append to diagonal vent list
        diagVentsList.append(vent)
    # Otherwise append to non-diagonal vent list
    else:
        notDiagVentsList.append(vent)

# Initialise empty list to hold sets of points of all horizontal and
# vertical vents
notDiagVentsPointsList = []
# Iterate over all horizontal and vertical vents
for vent in notDiagVentsList:
    # Initialise empty points set
    points = set()
    # Check if vent horizontal
    if vent[0][1] == vent[1][1]:
        # Iterate over each x coordinates for vent
        # Add 1 to top of range in order to include final point
        for x in range(min(vent[0][0], vent[1][0]),\
            max(vent[0][0], vent[1][0]) + 1):
            # Add x, y coordinate to points set
            points.add((x, vent[0][1]))
    # Otherwise vent is vertical
    else:
        # Iterate over each y coordinates for vent
        # Add 1 to top of range in order to include final point
        for y in range(min(vent[0][1], vent[1][1]),\
            max(vent[0][1], vent[1][1]) + 1):
            # Add x, y coordinate to points set
            points.add((vent[0][0], y))
    # Append set of points to list
    notDiagVentsPointsList.append(points)

# Initialise empty set to hold all points which correspond to intersection
# of 2 or more vents
pointsIntersectionSet = set()
# Iterate over index of non-diagonal vents points list
for idx1 in range(len(notDiagVentsPointsList)):
    # Iterate over index of non-diagonal vents points list, from idx1 onwards
    for idx2 in range(idx1+1, len(notDiagVentsPointsList)):
        # Identify coordinates of any intersecting points of the 2 vents
        # Add coordinates of intersecting points to intersection set
        pointsIntersectionSet.update(notDiagVentsPointsList[idx1].\
            intersection(notDiagVentsPointsList[idx2]))

# Print results summary
print(f'Count of points where at least 2 vents intersect: \
{len(pointsIntersectionSet)}')

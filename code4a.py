# Import pandas to read csv and numpy for matrix manipulation
import pandas as pd
import numpy as np

# Create dataframe from csv of random drawn numbers
df = pd.read_csv('task4a.csv', header=None, delimiter=',').transpose()
# Create list containing each row's entry
randomNumsList = [row[0] for row in df.to_numpy()]
# Print summary
print(f'Count of randomly drawn numbers: {len(randomNumsList)}')

# Create dataframe from csv of bingo boards
df = pd.read_csv('task4b.csv', header=None, delimiter=',')
# Initialise empty dataframe to add processed numbers
dfCols = pd.DataFrame()
# Iterate 0-4 (bingo board is size 5x5)
for i in range(5):
    # Create col in new dataframe for each bingo square
    # Split single string into constituent numbers and cast as integers
    dfCols[str(i)] = df[0].apply(lambda row: int(row[(i*3):(i*3+2)]))
# Cast dataframe to numpy array
boardsArray = dfCols.to_numpy()
# Reshape array to separate each 5x5 bingo board
# Each square accessed by indexing as [z][y][x]
boardsArray = np.reshape(boardsArray, (100,5,5))
print(f'Count of bingo boards: {boardsArray.shape[0]}\n')


# Function to check if board is now in a winning state
def winningBoardChecker(board):
    # Check board rows
    # Iterate over row indices
    for rowIdx in range(board.shape[0]):
        # Count unique values in row
        rowUniqueArray = np.unique(board[rowIdx,:], return_counts=True)
        # Check if the row is full of -1 values
        if rowUniqueArray[0][0] == -1 and \
            rowUniqueArray[1][0] == board.shape[1]:
            return True
    # Check board columns
    # Iterate over column indices
    for colIdx in range(board.shape[1]):
        # Count unique values in column
        colUniqueArray = np.unique(board[:,colIdx], return_counts=True)
        if colUniqueArray[0][0] == -1 and colUniqueArray[1][0] == 5:
            # Check if the row is full of -1 values
            return True


# Function to process all random numbers and find first winning bingo board
def numberBoardProcessor(randomNumsList, boardsArray):
    # Iterate over random drawn number list
    for num in randomNumsList:
        # Iterate over boards indices
        for boardIdx in range(boardsArray.shape[0]):
            # Iterate over board row indices
            for rowIdx in range(boardsArray.shape[1]):
                # Iterate over board column indices
                for colIdx in range(boardsArray.shape[2]):
                    # Check if current square value equals drawn number
                    if boardsArray[boardIdx, rowIdx, colIdx] == num:
                        # Change square value to -1, this will not be actual
                        # square value and marks the square as called
                        boardsArray[boardIdx, rowIdx, colIdx] = -1
            # Check if current board is now a winning board
            if winningBoardChecker(boardsArray[boardIdx]):
                # End loops
                # Return current board index and last number called
                return boardIdx, num
    # Print error message if no winner found
    print('All numbers called and no winner was found')

# Function to calculate winning board score
def boardScorer(board, finalNum):
    # Initialise a score count
    score = 0
    # Iterate over board row indices
    for rowIdx in range(board.shape[0]):
        # Iterate over board column indices
        for colIdx in range(board.shape[1]):
            # Check if value of current square is not -1
            # and has therefore not been called
            if board[rowIdx, colIdx] != -1:
                # Increase score by current square value
                score += board[rowIdx, colIdx]
    # Multiply by final number drawn to win
    return score * finalNum

# Find winning board and the final random number to be drawn in order to win
winningBoardIdx, finalNum = numberBoardProcessor(randomNumsList, boardsArray)
# Calulate winning board score
score = boardScorer(boardsArray[winningBoardIdx], finalNum)
# Print summary
print(f'Winning board number: {winningBoardIdx}\
    \n{boardsArray[winningBoardIdx]}\
    \nBoard score: {score}')

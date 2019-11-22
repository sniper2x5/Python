
def knightMove (row,column):
    """knightMove (row,column) - takes in a coordinate point on a chess board and returns all possible knight moves"""
    #Variables
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    spots = []
    moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
    column = letters.index(column)+1
    #Calculates Legal moves and appends into final list
    for i in moves:
        if 1 <= (column + i[0]) <= 8 and 1 <= (row + i[1]) <= 8:
                spots.append((row + i[1],letters[column + i[0]-1]))
    return spots
print knightMove(2,"F")
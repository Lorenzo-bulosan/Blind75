from collections import deque

def number_islands(grid: list[list[str]], recursive = True) -> int:

    if len(grid) == 0:
        return 0
    
    current = str()
    num_islands = 0
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            current = grid[r][c]

            if current == '1' and not (r,c) in visited:

                if recursive:
                    dfs(r, c, grid, visited)
                else:
                    dfs_iterative(r, c, grid, visited)
                num_islands += 1

    return num_islands 


def dfs_iterative(i, c, grid, visited):

    if i >= 0 and c >= 0 and i <= len(grid)-1 and c <= len(grid[i])-1 and grid[i][c] == '1' and (i,c) not in visited:

        visited.add((i,c)) 
        dfs_iterative(i+1, c, grid, visited)
        dfs_iterative(i-1, c, grid, visited)
        dfs_iterative(i, c+1, grid, visited)
        dfs_iterative(i, c-1, grid, visited)

    return


def dfs(i, c, grid, visited) -> None:

    st = deque()

    st.append((i,c))
    visited.add((i,c))

    neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
    row_lenght = len(grid)-1
    col_lenght = len(grid[0])-1

    while len(st) > 0:

        r, c = st.pop()

        for pr, pl in neighbors:
            x, y = r+pr, c+pl

            if x >= 0 and y >= 0 and x <= row_lenght and y <= col_lenght:
                if grid[x][y] == '1' and (x,y) not in visited:
                    visited.add((x,y))
                    st.append((x,y))

            # if is_valid_neighbor():
                

def test_number_islands_returns_correct_number_when_single_island():

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    actual = number_islands(grid)

    assert 1 == number_islands(grid)

def test_number_islands_returns_correct_number_when_multiple_islands():

    grid = [
        ["1","0","0","1"],
        ["0","1","0","1"]
    ]

    actual = number_islands(grid)

    assert 3 == number_islands(grid)

def test_number_islands_returns_correct_number_when_single_island_iterative():

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    # actual = number_islands(grid, False)

    assert 1 == number_islands(grid, False)

def test_number_islands_returns_correct_number_when_multiple_islands_iterative():

    grid = [
        ["1","0","0","1"],
        ["0","1","0","1"]
    ]

    # actual = number_islands(grid)

    assert 3 == number_islands(grid, False)

test_number_islands_returns_correct_number_when_single_island()
test_number_islands_returns_correct_number_when_multiple_islands()

test_number_islands_returns_correct_number_when_single_island_iterative()
test_number_islands_returns_correct_number_when_multiple_islands_iterative()
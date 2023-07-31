def pacific_atlantic_ocean(heights: list[list[int]]) -> list[list[int]]:
    
    rLength, cLength = len(heights), len(heights[0])
    vstPacific, vstAtl = set(), set()

    def dfs(r, c, prevHeight, vst):

        # out of bounds
        if(r < 0 or c < 0 or r >= rLength or c >= cLength) : #print('out of bounds')
            return

        # already visited
        if( (r,c) in vst ): # print('already visited')
            return

        # lower than previous
        if( prevHeight > heights[r][c] ): # print(prevHeight, heights[r][c])
            return

        # add to visit
        vst.add((r,c))

        # dfs into neighbors
        dfs(r+1, c, heights[r][c], vst)
        dfs(r-1, c, heights[r][c], vst)
        dfs(r, c+1, heights[r][c], vst)
        dfs(r, c-1, heights[r][c], vst)
        
    # dfs in vertical oceans starting top and bottom cols to dfs
    r = 0
    rLast = rLength - 1
    
    for c in range(cLength):
        
        currentTopRowHeight = heights[r][c]
        dfs(r, c, currentTopRowHeight, vstPacific)
        
        currentLastRowHeight = heights[rLast][c]
        dfs(rLast, c, currentLastRowHeight, vstAtl)
    
    # dfs in horizontal oceans starting left and rigth rows to dfs
    cFirst = 0
    cLast = cLength - 1
    for r in range(rLength):
        
        currentLeftColHeight = heights[r][cFirst]
        dfs(r, cFirst, currentLeftColHeight, vstPacific)
        
        currentRightColHeight = heights[r][cLast]
        dfs(r, cLast, currentRightColHeight, vstAtl)
    
    # find if which positions appear in both sets
    
    positionsReachedFromBothOceans = []
    for r, c in vstPacific:
        if((r,c) in vstAtl): 
            positionsReachedFromBothOceans.append([r,c])
            
    return positionsReachedFromBothOceans

def test_pacific_atlantic_ocean_only_1_island():

    heights = [[1]]

    assert [[0,0]] == pacific_atlantic_ocean(heights)

def test_pacific_atlantic_ocean():

    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    actual = pacific_atlantic_ocean(heights)

    # Order doesn't matter check that 'actual' has same pairs as 'expected'
    for i in range(len(expected)):
        if expected[i] not in actual:
            assert False
    
    assert True    

if __name__ == '__main__':

    test_pacific_atlantic_ocean_only_1_island()
    test_pacific_atlantic_ocean()
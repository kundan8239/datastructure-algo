""" 
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""

"""
    Example 
    Input: rowIndex = 3
    Output: [1,3,3,1]

    Input: rowIndex = 0
    Output: [1]

    Input: rowIndex = 1
    Output: [1,1]

"""

def getRow(self, rowIndex: int) -> List[int]:
    res = []
    for i in range(rowIndex + 1):
        res.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                res[i].append(1)
            else:
                res[i].append(res[i-1][j - 1] + res[i-1][j])
    return res[rowIndex]
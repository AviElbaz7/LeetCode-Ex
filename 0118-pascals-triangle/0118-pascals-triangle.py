class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            currRow = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    currRow.append(1)
                elif i > 1:
                    currRow.append(result[i-1][j-1] + result[i-1][j])
            result.append(currRow)
        return result
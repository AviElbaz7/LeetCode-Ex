class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hashmap = {}
        n = len(matrix) - 1
        for row in matrix:
            hashmap[n] = row
            n -= 1
        
        for i in range(len(matrix)):
            matrix[i] = hashmap[i]
        
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y=len(matrix)
        x=len(matrix[0])

        def todd(n):
            return matrix[(n-1)//x][(n-1)%x]

        def bst(low,high):
            if low>high:
                return False

            mid= (low + high) // 2
            result = todd(mid)
            if result == target:
                return True
            elif result > target:
                return bst(low, mid-1)
            else:
                return bst(mid+1, high)

        return bst(1, x*y)

        
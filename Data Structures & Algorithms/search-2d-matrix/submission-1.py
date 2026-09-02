class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        print('start')
        row = -1
        while l <= r:
            mid = l + (r - l) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
            if target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        if row == -1:
            False

        l = 0
        r = len(matrix[mid]) - 1
        while l <= r:
            newMid = l + (r-l)//2
            if target == matrix[mid][newMid]:
                return True
            
            elif target < matrix[mid][newMid]:
                r = newMid - 1
            else:
                l = newMid + 1
        return False





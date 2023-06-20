class Solution:
    def spiralOrder(self, matrix):
        ans = []
        matrix_size = len(matrix) * len(matrix[0])
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        def go_right():
            for i in range(left, right):
                ans.append(matrix[top][i])

        def go_down():
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])

        def go_left():
            for i in range(right - 1, left -1, -1):
                ans.append(matrix[bottom - 1][i])

        def go_up():
            for i in range(bottom - 1, top -1, -1):
                ans.append(matrix[i][left])

        while left < right and top < bottom:
            go_right()
            top += 1
            go_down()
            right -= 1
            if len(ans) == matrix_size:
                break
            go_left()
            bottom -= 1
            go_up()
            left += 1
            


        return ans  
    
solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
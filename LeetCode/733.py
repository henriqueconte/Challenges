class Solution:

    visitedImage = [[]]

    def floodFill(self, image, sr, sc, color):
        self.visitedImage = [[0 for i in range(len(image))] for j in range(len(image[0]))]
        self.floodPath(image, sr, sc, color)
        image[sr][sc] = color
        return image

    def floodPath(self, image, sr, sc, color):
        self.visitedImage[sr][sc] = 1
        
        # Going up
        if sr > 0 :
            if image[sr - 1][sc] == image[sr][sc] and self.visitedImage[sr - 1][sc] == 0:
                self.floodPath(image, sr - 1, sc, color)
                image[sr - 1][sc] = color

        # Going left
        if sc > 0: 
            if image[sr][sc - 1] == image[sr][sc] and self.visitedImage[sr][sc - 1] == 0:
                self.floodPath(image, sr, sc - 1, color)
                image[sr][sc - 1] = color

        # Going right
        if sc < len(image[0]) - 1:
            if image[sr][sc + 1] == image[sr][sc] and self.visitedImage[sr][sc + 1] == 0:
                self.floodPath(image, sr, sc + 1, color) 
                image[sr][sc + 1] = color

        # Going down
        if sr < len(image) - 1:
             if image[sr + 1][sc] == image[sr][sc] and self.visitedImage[sr + 1][sc] == 0:
                self.floodPath(image, sr + 1, sc, color)
                image[sr + 1][sc] = color
            
        return image
    

# Create auxiliary table filled with 0s
# Given a point, we will verify on the auxiliary table if we checked each of the 4 sides
# If we have already checked, move to the next side
# If we didn't check, replace the color if it's the same number  
solution = Solution()

print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
from typing import List


class Solution:

    def colorImage(self, sr, sc, originalColor, newColor):
        if sr < 0 or sc < 0 or sr >= len(self.image) or sc >= len(self.image[0]):
            return False

        #print(sr, sc)
        if self.image[sr][sc] != originalColor:
            return False

        if self.image[sr][sc] == originalColor:
            self.image[sr][sc] = newColor
            self.colorImage(sr-1, sc, originalColor, newColor)
            self.colorImage(sr+1, sc, originalColor, newColor)
            self.colorImage(sr, sc-1, originalColor, newColor)
            self.colorImage(sr, sc+1, originalColor, newColor)

        return True

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        self.image = image
        self.colorImage(sr, sc, originalColor, newColor)
        return self.image

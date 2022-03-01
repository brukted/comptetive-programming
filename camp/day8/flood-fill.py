class Solution:
    def __init__(self):
        self.dirVectors = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def coordsInRange(self, matrix, coords):
        return coords[0] >= 0 and coords[0] < len(matrix) and coords[1] >= 0 and coords[1] < len(matrix[0])

    def fillRec(self, image, sr, sc, newColor):

        oldColor = image[sr][sc]
        image[sr][sc] = newColor

        for dirVector in self.dirVectors:
            newCoords = (sr+dirVector[0], sc+dirVector[1])
            if self.coordsInRange(image, newCoords) and image[newCoords[0]][newCoords[1]] == oldColor:
                self.fillRec(image, newCoords[0], newCoords[1], newColor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fillRec(image, sr, sc, newColor)
        return image

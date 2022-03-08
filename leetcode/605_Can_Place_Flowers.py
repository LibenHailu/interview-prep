class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        canPlant = 0
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):

            if flowerbed[i-1:i+2] == [0, 0, 0]:
                canPlant += 1
                flowerbed[i] = 1

        return canPlant >= n

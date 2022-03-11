class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        is_empty = lambda x : not flowerbed[x] and ( x - 1 < 0 or not flowerbed[x-1]) and ( x + 1 == len(flowerbed) or not flowerbed[x + 1])
        if not n:
            return True
        for idx in range(len(flowerbed)):
            if is_empty(idx):
                flowerbed[idx] = 1
                n -= 1
                if not n:
                    break
        return not n
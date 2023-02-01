class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_grow_pairs = list(zip(plantTime, growTime))
        plant_grow_pairs.sort(key=lambda x: -x[1])
        ans = cum = 0
        for (plant, grow) in plant_grow_pairs:
            cum += plant
            ans = max(ans, cum + grow)
        return ans

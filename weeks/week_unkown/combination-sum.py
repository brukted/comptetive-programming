class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # @lru_cache(None)
        def combinationSumRec(i = 0, t = target):
            pick = []
            if t - candidates[i] == 0:
                pick.append([candidates[i]])
            elif t - candidates[i] > 0:
                com = combinationSumRec(i, t - candidates[i])
                for arr in com:
                    arr.append(candidates[i])
                pick += com
            
            dont = combinationSumRec(i + 1, t) if i != len(candidates) - 1 else []
            
            return dont + pick
        
        return combinationSumRec()
            
            

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {
            2 : ['a','b','c'],
            3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r','s'],
            8 : ['t','u','v'],
            9 : ['w','x','y','z']
        }
        
        def rec(digits):
            if len(digits) == 1:
                return mapp[int(digits)]
            
            ans = []
            
            l = rec(digits[1:])
            
            for ch in mapp[int(digits[0])]:
                for com in l:
                    ans.append(ch + com)
            return ans
        
        return rec(digits) if digits else []

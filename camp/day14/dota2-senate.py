class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_list = [None for s in range(len(senate))]
        
        count = {"R" : 0, "D" : 0}
        
        for i, s in enumerate(senate):
            count[s] += 1
            senate_list[i] = s
        ban = ("R", 0)
        
        while True:
            for i , s in enumerate(senate_list):
                if not s: # Banned
                    continue
                
                if ban[1] > 0 and ban[0] == s: # To ban
                    senate_list[i] = None
                    ban = ban[0] , ban[1] - 1
                    count[ban[0]] -= 1
                    continue
                
                if s == "R" and not count["D"]:
                    return "Radiant"
                if s == "D" and not count["R"]:
                    return "Dire"
                ban = "R" if s == "D" else "D" , ban[1] + 1
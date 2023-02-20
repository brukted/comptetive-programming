class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def make_state_key(state):
            return "#".join(map(str, state.items())).strip()

        @cache
        def solve(state_key, curr):
            if len(state_key) == 0:
                return 0
            
            if curr == len(stickers):
                return inf

            state = {}
            for part in state_key.split("#"):
                a, b = part[1:-1].split(',')
                state[a.strip()[1:-1]] = int(b)

            worth_it = False
            next_state = state.copy()

            for ch in stickers[curr]:
                if ch in next_state:
                    next_state[ch] -= 1
                    worth_it = True
                
                if ch in next_state and next_state[ch] == 0:
                    next_state.pop(ch)
            
            next_state_key = make_state_key(next_state)
            
            if worth_it:
                return min(1 + min(solve(next_state_key, curr), solve(next_state_key, curr + 1)), solve(state_key, curr + 1))
            
            return solve(state_key, curr + 1)
        
        ans = solve(make_state_key(Counter(target)), 0) 
        return ans if ans != inf else -1

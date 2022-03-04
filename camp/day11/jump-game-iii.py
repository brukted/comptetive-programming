class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        def is_inbound(x): return 0 <= x < len(arr)

        bfsDeq = deque([start])
        visited = {start}

        while bfsDeq:
            idx = bfsDeq.popleft()
            a = idx + arr[idx]
            if is_inbound(a) and a not in visited:
                if arr[a] == 0:
                    return True
                visited.add(a)
                bfsDeq.append(a)

            b = idx - arr[idx]
            if is_inbound(b) and b not in visited:
                if arr[b] == 0:
                    return True
                visited.add(b)
                bfsDeq.append(b)

        return False

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            task.append(idx)
        
        tasks.sort()
        time = curr = 0
        queue = []
        result = []
        
        while curr < len(tasks) or queue:
            while curr < len(tasks) and tasks[curr][0] <= time + 1:
                heappush(queue, (tasks[curr][1], tasks[curr][2]))
                curr += 1
            
            if not queue:
                time = tasks[curr][0] - 1
            else:
                p, idx = heappop(queue)
                time += p
                result.append(idx)

        return result


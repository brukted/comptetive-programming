class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}
        
        def findParent(i):
            if parents[i] == i:
                return i
            p = findParent(parents[i])
            parents[i] = p
            return p
        
        def connect(place1,place2):
            root_1 = findParent(place1)
            root_2 = findParent(place2)
            if root_1 != root_2:
                parents[root_1] = root_2
        
        for next_id, account in enumerate(accounts):
            name = account[0]
            group = None
            for i in range(1,len(account)):
                if account[i] in parents:
                    group = findParent(account[i])
                    break
            
            if group == None:
                group = next_id
                parents[group] = group
            
            for i in range(1,len(account)):
                if account[i] in parents:
                    connect(account[i],group)
                else:
                    parents[account[i]] = group
        
        for i in parents.keys():
            findParent(i)
        
        grouped = defaultdict(list)
        for i in parents.items():
            if not isinstance(i[0],int):
                grouped[i[1]].append(i[0])
        
        ans = []
        for item in grouped.items():
            name = accounts[item[0]][0]
            ans.append([name])
            ans[-1] += sorted(item[1])
        
        return ans

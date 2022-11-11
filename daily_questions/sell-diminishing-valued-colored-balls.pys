class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse = True)
        inventory.append(0)
        mod = 10 ** 9 + 7
        n = len(inventory)
        ans = 0
        
        for index in range(1, n):
            if orders == 0:
                break
            
            diff = inventory[index - 1] - inventory[index]
            count = index
            full_diffs = min(orders // count, diff)
            
            if full_diffs != 0:
                ans = (ans + (count * full_diffs * (2 * inventory[index - 1] - full_diffs + 1)) // 2) % mod
                orders -= count * full_diffs
                inventory[index - 1] -= full_diffs
            
            if inventory[index - 1] > inventory[index]:
                ans = (ans + (inventory[index - 1] * orders) % mod) % mod
                orders = 0
        
        return ans % mod
            
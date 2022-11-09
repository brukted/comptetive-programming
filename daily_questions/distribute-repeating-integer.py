class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = list(map(lambda x: x[1], Counter(nums).items()))
        all_satisfied = (1 << len(quantity)) - 1

        @lru_cache(None)
        def solve(statified_customers=0, i=0, reduced=0):
            if statified_customers == all_satisfied:
                return True

            if i == len(count):
                return False

            for customer in range(len(quantity)):
                if (statified_customers & 1 << customer) or count[
                    i
                ] - reduced < quantity[customer]:
                    continue

                if solve(
                    statified_customers | (1 << customer),
                    i,
                    reduced + quantity[customer],
                ):
                    return True

            return solve(statified_customers, i + 1)

        return solve()

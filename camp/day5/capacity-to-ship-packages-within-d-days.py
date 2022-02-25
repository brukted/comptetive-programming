class Solution:
    def howManyDays(self, weights, capacity):
        days = 0
        load = 0
        j = 0
        while j < len(weights):
            if load + weights[j] > capacity:  # Cant hold
                days += 1
                load = weights[j]

            elif load + weights[j] < capacity:  # There is a space
                load += weights[j]

            else:  # Right on it
                days += 1
                load = 0
            j += 1

        if load:
            days += 1
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        a ship with a capacity of the max of the packages would take the maximum time
        a ship with a capacity of the sum of the packages would take one day
        calculate how many days it will take
        """
        left = max(weights)  # Would take max days
        right = sum(weights)  # Would take min days
        while left < right:
            mid = (left+right)//2
            days_to_take = self.howManyDays(weights, mid)
            if days_to_take > days:  # Not acceptable
                left = mid + 1
            else:
                right = mid
        return right

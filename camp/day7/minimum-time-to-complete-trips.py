class Solution:
    def getTrips(self, tripTime, time):
        return tripTime // time

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 0
        right = max(time) * totalTrips

        best = None

        while left <= right:
            mid = (left+right) // 2
            total_trips_taken = 0

            for t in time:
                total_trips_taken += self.getTrips(mid, t)

            if total_trips_taken < totalTrips:
                left = mid + 1
            else:
                right = mid - 1
                best = mid

        return best

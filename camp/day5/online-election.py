class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

        self.winners = [persons[0]]
        votes = {persons[0]: 1}
        lastWinner = (persons[0], 1)

        for i in range(1, len(times)):
            voted_person = persons[i]
            vote_time = times[i]

            if voted_person in votes:
                votes[voted_person] += 1
            else:
                votes[voted_person] = 1

            if votes[voted_person] >= lastWinner[1]:
                lastWinner = (voted_person, votes[voted_person])

            self.winners.append(lastWinner[0])

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        best = -1

        # Find the last vote that was made just before t or at t -- O(log(n))
        while left <= right:
            mid = (left + right) // 2

            if self.times[mid] > t:  # mid is way off from t
                right = mid - 1
            else:  # mid smaller or at t
                left = mid + 1
                best = mid

        return self.winners[best]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

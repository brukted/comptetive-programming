class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = [room for room in range(n)]
        meetings_held = {room: 0 for room in range(n)}
        rooms_held = []

        meetings.sort()

        for (start, end) in meetings:
            while rooms_held and rooms_held[0][0] <= start:
                heappush(free_rooms, heappop(rooms_held)[1])

            room, room_end = 0, 0

            if not free_rooms:
                room_end, room = heappop(rooms_held)
            else:
                room_end, room = start, heappop(free_rooms)

            meetings_held[room] += 1
            heappush(rooms_held, (end + room_end - start, room))

        return max(meetings_held.items(), key=lambda x: (x[1], -x[0]))[0]

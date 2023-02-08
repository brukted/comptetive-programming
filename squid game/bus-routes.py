class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        buses = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                buses[stop].append(bus)

        final_bus = set(buses[target])
        start_buses = buses[source]

        visited = set(start_buses)
        queue = deque(map(lambda bus: (bus, 1), start_buses))

        while queue:
            bus, count = queue.popleft()

            if bus in final_bus:
                return count

            for stop in routes[bus]:
                for next_bus in buses[stop]:
                    if next_bus not in visited:
                        queue.append((next_bus, count + 1))
                        visited.add(next_bus)

        return -1


2

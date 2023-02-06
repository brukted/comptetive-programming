class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = {(0, 1)}

        while queue:
            pos, speed, length = queue.popleft()

            if pos == target:
                return length

            if (pos + speed, speed * 2) not in visited and pos + speed <= target * 2:
                queue.append((pos + speed, speed * 2, length + 1))
                visited.add((pos + speed, speed * 2))

            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in visited:
                queue.append((pos, new_speed, length + 1))
                visited.add((pos, new_speed))

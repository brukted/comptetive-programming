class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        furthest = 0
        bricks_used = []  # A max heap to keep track of jumps made using bricks
        ladders_used = []  # A min heap to keep track of jumps made using ladders

        while furthest < len(heights) - 1:
            diff = heights[furthest+1] - heights[furthest]

            if diff <= 0:  # No brick or ladders needded
                furthest += 1
                continue

            if bricks < diff:  # Not enough bricks
                highest_jump_with_brick = 0  # Highest that could have used a ladder
                # Smallest that could have used bricks
                smallest_jump_with_ladder = float("inf")

                if bricks_used:
                    highest_jump_with_brick = -bricks_used[0]
                if ladders_used:
                    smallest_jump_with_ladder = ladders_used[0]

                if highest_jump_with_brick + bricks >= diff and ladders > 0:  # Can replace with ladder
                    # Replace with ladder
                    bricks -= heapq.heappop(bricks_used)
                    ladders -= 1
                    heapq.heappush(ladders_used, highest_jump_with_brick)

                    # Make jump using bricks
                    bricks -= diff
                    heapq.heappush(bricks_used, -diff)
                    furthest += 1

                elif ladders > 0:  # Use ladder only
                    heapq.heappush(ladders_used, diff)
                    furthest += 1
                    ladders -= 1

                elif smallest_jump_with_ladder <= bricks:  # Use avilable bricks to save a ladder
                    print("Saved a ladder", bricks, smallest_jump_with_ladder)
                    # Save a ladder
                    heapq.heappop(ladders_used)
                    ladders += 1
                    bricks -= smallest_jump_with_ladder
                    heapq.heappush(bricks_used, -smallest_jump_with_ladder)

                    # Make jump using the saved ladder
                    ladders -= 1
                    furthest += 1

                else:  # Can't replace with ladder or use a ladder
                    break

            else:
                bricks -= diff
                heapq.heappush(bricks_used, -diff)
                furthest += 1

        return furthest

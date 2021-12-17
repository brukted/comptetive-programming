# https://www.hackerrank.com/challenges/counting-valleys/problem

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    altitude = 0
    vallies = 0
    for step in path:
        if step == 'D':
            altitude -= 1
        else:
            altitude += 1
            if altitude == 0:
                vallies += 1
    return vallies

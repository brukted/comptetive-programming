# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW = 1
        COL = 2
        mode = ROW
        first = True
        result = []
        uL = (0,  0)
        lR = (len(matrix)-1,  len(matrix[0])-1)
        target = len(matrix) * len(matrix[0])
        while len(result) < target:
            print("Matrix",  matrix)
            if mode == ROW:
                print("ROW")
            else:
                print("COL")
            print("First {}".format(first))
            print("uL : {}, lR : {}".format(uL,  lR))

            if mode == ROW:
                if first:
                    result += matrix[uL[0]][uL[1]:lR[1]+1]
                    uL = (uL[0]+1,  uL[1])
                    mode = COL
                    first = False
                else:
                    result += matrix[lR[0]][lR[1]:uL[1]-1]
                    lR = lR[0] -  1 , lR[1]
                    mode = COL
                    first = True
            else:
                if first:
                    for i in range(lR[0],  uL[0]+1 , -1):
                        result.append(matrix[i][uL[1]])
                    uL = uL[0],  uL[1]+1
                    mode = ROW
                else:
                    for i in range(uL[0],  lR[0]+1):
                        result.append(matrix[i][lR[1]])
                    lR = lR[0],  lR[1]-1
                    mode = ROW
            print("Result",  result)
            print("-------------------------")

        return result

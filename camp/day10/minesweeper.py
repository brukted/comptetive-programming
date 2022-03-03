class Solution:
    def __init__(self):
        self.DIR_VECS = [(-1, 0), (1, 0), (0, -1), (0, 1),
                         (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def isInBound(self, board, pos):
        return 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0])

    def dfsClick(self, board, pos):
        if board[pos[0]][pos[1]] in {'X', 'M', 'B'}:
            return

        # square is E
        neighbour_mines = 0
        for vec in self.DIR_VECS:
            i, j = pos[0] + vec[0], pos[1] + vec[1]
            if self.isInBound(board, (i, j)) and (board[i][j] == 'X' or board[i][j] == 'M'):
                neighbour_mines += 1

        if neighbour_mines == 0:
            board[pos[0]][pos[1]] = 'B'
            for vec in self.DIR_VECS:
                i, j = pos[0] + vec[0], pos[1] + vec[1]
                if self.isInBound(board, (i, j)) and board[i][j] == 'E':
                    self.dfsClick(board, (i, j))
        else:
            board[pos[0]][pos[1]] = str(neighbour_mines)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        si, sj = click
        if board[si][sj] == 'M':
            board[si][sj] = 'X'
            return board

        self.dfsClick(board, (si, sj))
        return board

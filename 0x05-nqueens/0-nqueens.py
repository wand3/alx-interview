#!/usr/bin/python3
"""
   N-Queens test
   Algorithm back tracking
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    result = []
    if r == n:
        for i in range(n):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    result.append([i, j])
        print(result)
        return
    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0

def nqueens(n):
    cols = set() #colums of chessboard
    pos_diag = set() #diagonal / down to top (row + col)
    neg_diag = set() #diagonal \ top down (row - col)
    board = [[0] * n for _ in range(n)]
    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

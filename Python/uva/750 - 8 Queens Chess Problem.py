import sys

def place(r, c):
    for i in range(c):
        if row[i] == r or (abs(row[i] - r) == abs(i - c)):
            return False
    return True

def backtrack(c):
    global line_counter
    if c == 8 and row[b] == a:
        temp = ""
        for j in range(1, 8):
            temp += " %d" % (row[j] + 1)
        print("%2d      %d%s" % (line_counter, row[0] + 1, temp))
        line_counter += 1
    for r in range(8):
        if place(r, c):
            row[c] = r
            backtrack(c + 1)

if __name__ == '__main__':
    t = int(input().strip())
    input()
    inputs = [sys.stdin.readline() for _ in range(2*t - 1)]
    for inp in inputs:
        if len(inp.strip()) == 0:
            continue
        row = [0] * 8
        line_counter = 1
        a, b = map(int, inp.split())
        a -= 1
        b -= 1
        print("SOLN       COLUMN")
        print(" #      1 2 3 4 5 6 7 8")
        print()
        backtrack(0)
        if inp != inputs[-1]:
            print()
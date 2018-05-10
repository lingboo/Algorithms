import sys

nums = []
f = sys.stdin
for line in f.readlines():
    nums.append(line.split())
    print(nums)
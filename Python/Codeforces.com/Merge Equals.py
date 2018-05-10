import queue
n = int(input().strip())
arr = list(map(int, input().split()))
pq = queue.PriorityQueue()
for i in range(n):
    pq.put((arr[i], i))


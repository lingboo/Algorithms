import queue
n = int(input().strip())
graph = [[] for _ in range(n)]
probabilities = [1.0]*n
dist = [0]*n
visited = [False]*n
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
q = queue.Queue()
q.put(0)
sum_ = 0
while not q.empty():
    top = q.get()
    count = 0
    visited[top] = True
    if len(graph[top]) == 1 and top != 0:
        sum_ += dist[top]*probabilities[top]
    for i in graph[top]:
        if not visited[i]:
            count += 1
    for i in graph[top]:
        if not visited[i]:
            dist[i] = dist[top] + 1
            probabilities[i] = probabilities[top]/count
            q.put(i)
print("{0:.15f}".format(sum_))
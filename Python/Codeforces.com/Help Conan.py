import queue
T = int(input().strip())
INF = 10**9
for _ in range(T):
    n, m, k = map(int, input().split())
    graph = [[] for i in range(n)]
    dist = [INF]*n
    visited = [False]*n
    for __ in range(n):
        u, v, c = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((c, v))
        graph[v].append((c, u))
    importance = list(map(int, input().split()))
    pq = queue.PriorityQueue()
    pq.put((0, 0))
    dist[0] = 0
    while not pq.empty():
        current = pq.get()
        node = current[1]
        visited[node] = True
        for neighbor in graph[node]:
            d_neighbor = neighbor[0]
            node_neighbor = neighbor[1]
            if not visited[node_neighbor] and dist[node_neighbor] > d_neighbor:
                dist[node_neighbor] = d_neighbor
                pq.put((dist[node_neighbor], node_neighbor))
    res = 0
    for im in importance:
        res += dist[im-1]
    print(res)
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(1, t+1):
        ans = ""
        N, T = map(int, input().split())
        words = []
        graph = []
        for __ in range(N):
            graph.append([])
            w = input().strip()
            words.append(w)
            for i in range(T):
                graph[__].append(w[i])
        if T <= 1:
            print("Case #%d: -" % _)
        else:
            print(graph)
            temp = ""
            for i in range(N):
                for j in range(T):
                    temp += graph[i][j]

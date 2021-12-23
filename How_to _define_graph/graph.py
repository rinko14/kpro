#隣接リスト
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n):
    u, v, w = map(int, input().split())
    graph[u-1].append([v-1, w])
    #graph[v-1].append([u-1, w])  # 有向グラフなら消す
print(graph)  # [[2, 3], [3, 1], [5, 9]], ..., [...]]

#隣接グラフ
n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    #graph[v-1][u-1] = w  # 有向グラフなら消す
print(graph)  # [[0, 2, 3, 0, 1], ..., [2, 0, 3, 0, 0]

#隣接リスト to 隣接グラフ
graph_new = [[0]*n for _ in range(n)]  # 隣接行列
for i, g_i in enumerate(graph):
    for j in g_i:
        graph_new[i][j] = 1
print(graph_new)

#隣接行列 to 隣接リスト
graph_new = []
for i in range(n):
    tmp_l = []
    for j in range(n):
        if graph[i][j] > 0:
            tmp_l.append(j)
    graph_new.append(tmp_l)
print(graph_new)

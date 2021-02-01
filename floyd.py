#V: số đỉnh input
#graph: ma trận đầu vào
import sys
sys.stdin = open('D:/src/DA_algo/inp.txt', 'r')


def floydwarshall(graph,dist, V, path):
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and i != j:
                path[i][j] = i
            else:
                path[i][j] = -1
    '''
    print("\nKẾT QUẢ MA TRẬN PATH TRƯỚC KHI CHẠY\n")
    for i in range(V):
        print(path[i])
    '''

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
    for i in range(V):
        if dist[i][i] < 0:
            return False
        
    return True 

#traceback

V = int(input())
graph = [[None for i in range(V)] for j in range(V)]
dist  = [[None for i in range(V)] for j in range(V)]
path = [[None for i in range(V)] for j in range(V)]
INF = int(1e9)
MAX = 100

for i in range(V):
    line = list(map(int, input().split()))
    for j in range(V):
        graph[i][j] = INF if line[j] == 0 and i!=j else line[j]
'''
for i in range(V):
    print(graph[i])
'''


floydwarshall(graph,dist, V, path)

'''
print("\nKẾT QUẢ MA TRẬN DIST SAU KHI CHẠY\n")
for i in range(V):
    print(dist[i])
'''
print("\nKẾT QUẢ MA TRẬN PATH SAU KHI CHẠY\n")

for i in range(V):
    print(path[i])


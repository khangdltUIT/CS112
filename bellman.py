import sys
import queue
sys.stdin = open('D:/src/DA_algo/inp_bellman.txt', 'r')

INF = 10**9
MAX = 105

class edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


n, m = map(int, input().split())
#n: số đỉnh m: số cạnh
def BellmanFord(s, dist, path):
    dist[s] = 0
    for i in range(1, n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v] :
                dist[v] = dist[u] + w
                path[v] = u
    return 

def traceback(path, source, destination):
    flag = destination
    res = []
    while flag != -1:
        res.append(flag)
        flag = path[flag]
    print("path: ", path[:n])
    '''
    for i in range(len(res)-1, 0, -1):
        print(res[i], end = '->')
    print(destination)
    '''
    return 
        
if __name__ == '__main__':
    
    graph = []
    #đồ thị đầu vào
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(edge(u, v, w))
    
    #Đường đi từ đỉnh 0 đến tất cả đỉnh còn lại:
    for s in range(n):
        dist = [INF for _ in range(MAX)]
        #ma trận trọng số nhỏ nhất từ đỉnh i đến đỉnh j
        path = [-1 for _ in range(MAX)]
        #lưu vết đường đi
        res = BellmanFord(s, dist, path)
        
        print("Đỉnh: ", s)
        for d in range(n):
            if (d != s):
                #print("Trọng số đường đi ngắn nhất từ đỉnh {} đến đỉnh {} : {} ".format(s, d, dist[d]))
                traceback(path, s, d)
                break
        
    
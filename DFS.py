import queue
import threading
MAX = 100000
graph = [[] for i in range(MAX)]
visited = [False for i in range(MAX)]
def dfs(node):
    s = queue.LifoQueue()
    s.put(node)
    while not s.empty():
        curr_node = s.get()
        if not visited[curr_node]:
            visited[curr_node] = True
            print(curr_node, end=" ")
            for adj_node in graph[curr_node]:
                if not visited[adj_node]:
                    s.put(adj_node)
def main():
    n, m, start_node = map(int, input("Enter No of Node, Edges, and start node: ").split())
    print("Enter Pair of edges:")
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(n):
        visited[i] = False
    dfs(start_node)
if __name__ == "__main__":
    threading.Thread(target=main).start()

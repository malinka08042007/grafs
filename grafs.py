class Graf():
    def __init__(self):
        self.graf={}
    def svuzy(self,u,v):
        if u not in self.graf:
            self.graf[u]=[]
        if v not in self.graf:
            self.graf[v]=[]
        self.graf[u].append(v)
        self.graf[v].append(u)
        print(self.graf[u])
        print(self.graf[v])
def dfs(graph, start, visited): #Обход в глубину
    visited.add(start)
    print(start)
    for neighbor in graph.graf[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
def bfs(graph, start): #Обход в ширину
    visited = set()
    ochered = [start]
    while ochered: #пока очередь не пустая 
        posled_vershina=ochered.pop(0) #извлекаем последний эл.
        if posled_vershina not in visited:
            print(posled_vershina,end='-')
            visited.add(posled_vershina)
            for neighbor in graph.graf[posled_vershina]:
                if neighbor not in visited:
                    ochered.append(neighbor)

#создание графа 
g=Graf()
g.svuzy(0,1)
g.svuzy(0,2)
g.svuzy(1,3)
g.svuzy(2,4)
g.svuzy(3,5)
g.svuzy(6,1)
g.svuzy(6,2)
g.svuzy(6,3)
g.svuzy(7,6)
g.svuzy(8,7)
g.svuzy(8,3)
g.svuzy(9,7)
g.svuzy(9,6)
visited=set()
dfs(g, 0,visited)
bfs(g,0)







class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + " -> " + self.dest.getName()
    
class Digraph(object):
    """edges is a dictionary that maps nodes to their children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src, dest = edge.getSource(), edge.getDestination()
        if not (src in self.edges or dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + ' -> ' + dest.getName() + '\n'
        return result[:-1] #omit final empty line added
        
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
def DFS(graph, start, end, path, shortest):
    """Find the shortest path from the start node to the end node using deep first search"""
    path = path + [start]
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: 
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result

def BFS(graph, start, end, toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path:', printPat)
    
def shortestPath(graph, start, end):
    return DFS(graph, start, end, [], None)


nodes = [Node('0'), Node('1'), Node('2'), Node('3')]

graph = Digraph()
graph.addNode(nodes[0])
graph.addNode(nodes[1])
graph.addNode(nodes[2])
graph.addNode(nodes[3])

graph.addEdge(Edge(nodes[0], nodes[1]))
graph.addEdge(Edge(nodes[0], nodes[3]))
graph.addEdge(Edge(nodes[1], nodes[2]))
graph.addEdge(Edge(nodes[2], nodes[3]))

path = shortestPath(graph, nodes[0], nodes[3])
for node in path:
    print(node)
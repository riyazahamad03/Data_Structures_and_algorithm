class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacencyList={}

    def __str__(self):
        return str(self.__dict__)

    def addVertex(self,node):
        self.adjacencyList[node] = []
        self.numberOfNodes+=1
    
    def addEdge(self,node1,node2):
        self.adjacencyList[node1].append(node2)
        self.adjacencyList[node2].append(node1)


    def conn(self):
        for v,n in self.adjacencyList.items():
            print(v,end='-->')
            print(" ".join(n))
MyGraph = Graph()
MyGraph.addVertex('0')
MyGraph.addVertex('1')
MyGraph.addVertex('2')
MyGraph.addVertex('3')
MyGraph.addVertex('4')
MyGraph.addVertex('5')
MyGraph.addVertex('6')
MyGraph.addEdge('3', '1')
MyGraph.addEdge('3', '4')
MyGraph.addEdge('4', '2') 
MyGraph.addEdge('4', '5') 
MyGraph.addEdge('1', '2') 
MyGraph.addEdge('1', '0') 
MyGraph.addEdge('0', '2') 
MyGraph.addEdge('6', '5')
print(MyGraph)
MyGraph.conn()
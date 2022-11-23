class Node:
    def __init__(self, value, edgeList = []):
        self.value = value
        self.edgeList = edgeList

    def connect(self, node):
        self.edgeList.append(node)
        node.edgeList.append(self)
    def getAdjacentNode(self, edges = []):
        for edge in self.edgeList:
            edges.append(edge.value)
        return edges

    def isConnected(self, node):
        for edge in self.edgeList:
            if edge.value == node.value:
                return True
        return False

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def addToGraph(self, node):
        self.nodes.append(node)

    def reconstructPath(self, visitedNodes, start, end):
        currNode = end
        shortestPath = []
        while currNode:
            print(currNode.value)
            shortestPath.append(currNode)
            currNode = visitedNodes[currNode.value]
        return shortestPath


    def breadthFirstTraversal(self, start, end):
        queue = [start]
        visitedNodes = {}
        visitedNodes[start.value]  = None
        while len(queue)>0:
            node = queue.pop()
            # print(node.value)
            if node.value == end.value:
                print('Found it..!')
                return self.reconstructPath(visitedNodes, start, end)
            for adjacency in node.edgeList:
                if adjacency.value not in visitedNodes.keys():
                    visitedNodes[adjacency.value] = node
                    queue.append(adjacency)

        print(visitedNodes)


if __name__ == '__main__':
    Hannah = Node('Hannah')
    Mary = Node('Mary')
    Mel = Node('Mel')
    Max = Node('Max')
    Dan = Node('Dan')
    Nis = Node('Nis')
    Chris = Node('Chris')
    Nicolette = Node('Nicolette')
    Yair = Node('Yair')
    Mabel = Node('Mabel')
    Liz = Node('Liz')

    graph = Graph([Hannah, Mary, Mel, Max, Dan, Nis, Chris, Nicolette, Yair, Mabel, Liz])

    Hannah.connect(Max)
    Hannah.connect(Mel)
    Hannah.connect(Mary)
    Hannah.connect(Nis)
    Hannah.connect(Liz)
    Mel.connect(Max)
    Nis.connect(Dan)
    Nis.connect(Chris)
    Nis.connect(Yair)
    Chris.connect(Nicolette)
    Chris.connect(Yair)
    Yair.connect(Mabel)
    Yair.connect(Liz)
    Mabel.connect(Liz)


    path = graph.breadthFirstTraversal(Hannah, Mabel)

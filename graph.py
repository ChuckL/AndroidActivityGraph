class Graph():
	"""docstring for Graph"""

	graphDictionary = {}

	def __init__(self):
		super(Graph, self).__init__()
	
	def addNode(node):
		if node not in graphDictionary:
			graphDictionary[node] = []
	
	def addEdge(fromNode, toNode):
		if node in graphDictionary:
			graphDictionary[node].append((fromNode, toNode));
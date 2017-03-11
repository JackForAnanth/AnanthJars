import networkx as nx

def func( jars, jars_size):

	if( jars[0] < jars_size[0] ):
		yield jars_size[0], jars[1]

	# Fill jug2
	if( jars[1] < jars_size[1]):
		yield jars[0], jars_size[1]

	# Fill jug1 to jug2
	toFill = min(jars[0], jars_size[1] - jars[1])
	if( toFill > 0 ):
		yield jars[0] - toFill, jars[1] + toFill

	# Pour jug2 to jug1
	toFill = min(jars[1], jars_size[0] - jars[0] )
	if( toFill > 0 ):
		yield jars[0] + toFill, jars[1] - toFill

	#empty jug1
	if( jars[0] > 0 ):
		yield 0, jars[1]

	if( jars[1] > 0 ):
		yield jars[0], 0

Graph = nx.DiGraph()

def add_connection(Graph, jar, newjar, jar_size):
    if not Graph.has_edge(jar, newjar):
        Graph.add_edge(jar, newjar)
        build_gallon_graph(Graph, newjar, jar_size)

def build_gallon_graph(Graph, jar, jar_size):
    for newjar in func(jar, jar_size):
        add_connection(Graph, jar, newjar, jar_size)

sizes = raw_input("Please enter the Jar1 & Jar2 capacities (separated by a ' '): ").split(' ')
goal = int(raw_input("Enter the desired quantity (volume) of fluid: "))

sizes = ( int(sizes[0]) , int(sizes[1]) )


start = (0,0)
build_gallon_graph( Graph, start , sizes )
path = nx.shortest_path( Graph, start , (0,goal) )

for i in range(0, max(sizes)+1):
	if( i <= sizes[0]):
		if( not Graph.has_node((i,goal)) ):
			continue
		newPath = nx.shortest_path(Graph, start, (i,goal) )
		if( len( newPath ) < len(path) ):
			path = newPath
	if( i <= sizes[1]):
		if( not Graph.has_node( (goal,i) ) ):
			continue
		newPath = nx.shortest_path(Graph, start, (goal,i) )
		if( len( newPath ) < len(path) ):
			path = newPath

for item in path:
	print ("Jug1: {} and Jug2: {}".format(item[0], item[1]))
"find all paths from start to goal in graph"

def search(start, goal, graph):
	solns = []
	generate([start], goal, solns, graph)
	solns.sort(key=lambda x: len(x))
	return solns

def generate(path, goal, solns, graph):
	state = path[-1]
	if state == goal:
		solns.append(path)
	else:
		for arc in graph[state]:
			if arc not in path:
				

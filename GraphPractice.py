from graph import *
from graph.visuals import plot_2d

#Create Graph
g = Graph()


#node = vertex
# dict vtx: {vtxs edges to}
g.from_list([(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)])
number = g.nodes()

print(g)
plot = plot_2d(g)
plot.show()
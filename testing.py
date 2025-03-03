from graph import *
from graph.visuals import plot_2d
from graph.random import random_xy_graph
from math import sin,cos,pi
from solver import GameState, Minimax

#Create Graph
g = Graph(from_list=[(1,2,0),(1,3,0),(1,4,0),(2,3,0),(2,4,0),(3,4,0)])

g2 = Graph(from_list=[(1,2,0),(1,3,0)])

g3 = Graph(from_list=[(1,2,0),(2,3,0),(3,4,0),(4,5,0),(5,6,0),(6,7,0),(7,8,0),(8,1,0),(1,5,0),(2,6,0),(3,7,0),(4,8,0)])


def viz(graph:Graph):
    node_count = len(graph.nodes())
    x_max = node_count * 8
    y_max = node_count * 4
    xygraph = random_xy_graph(node_count, x_max, y_max, edges=0, seed=10)
    mapping = {b:a for a,b in zip(xygraph.nodes(), graph.nodes())}
    for edge in graph.edges():
        start, end, distance = edge
        xygraph.add_edge(mapping[start], mapping[end], distance)
    
    plt = plot_2d(xygraph)
    plt.show()


def cycleViz(g:Graph):
    n = len(g.nodes())
    rad = 5
    angle = 2.0 * pi /(float(n))
    
    circle = [(rad*cos(angle*float(i)),rad*sin(angle*(float(i)))) for i in range(0,n)]

    mapping = {a:b for a,b in zip(g.nodes(),circle)}

    newEdges = [(mapping[start],mapping[end],value) for (start,end,value) in g.edges()]

    vizGraph = Graph(from_list=newEdges)

    plt = plot_2d(vizGraph)
    plt.show()



def allGraphs(n:int)->list[Graph]:

    

    #generate all possible matchings

    def matchingGen(vertices:set):
        if len(vertices) == 0:
            return [[]]
        elif len(vertices) % 2==1:
            ValueError(f"{len(vertices)} is odd")
        else:
            result = []
            start = vertices.pop()
            for end in vertices:
                newVertices = vertices.copy()
                newVertices.remove(end)
                for matching in matchingGen(newVertices):
                    matching.append((start,end,0))
                    matching += [(end,start,value) for (start,end,value) in matching]
                    result.append(matching)
            return result 
        

    out = []
    for matching in matchingGen(set(range(0,n))):
        cyc = cycle(n)
        cyc.from_list(matching)

        out.append(cyc)
    return out




def cycle(n:int)->Graph:
    cycle = [(i,(i+1) % n,0) for i in range(0,n)]

    out = Graph(from_list=cycle)
    out.from_list([(end,start,value) for (start,end,value) in cycle])

    return out

def LCF(chordList:list[int])->Graph:
    assert(len(chordList) % 2 == 0)
    n = len(chordList)
    cyc = cycle(n)

    chords = [(i,(i + chordList[i]) % n,0) for i in range(0,len(chordList))]

    cyc.from_list(chords)

    return cyc


g4 = Graph(from_list=[(1,2,0),(2,3,0),(3,4,0),(4,5,0)])

# tetra = LCF([2,2,2,2])
# utility = LCF([3,3,3,3,3,3])
# cubical = LCF([3,-3,3,-3,3,-3,3,-3])
# wagner = LCF([4,4,4,4,4,4,4,4])
# bidakis = LCF([-3,6,4,-4,6,3,-4,6,-3,3,6,4])
# franklin = LCF([5,-5,5,-5,5,-5,5,-5,5,-5,5,-5])
# frucht = LCF([-5,-2,-4,2,5,-2,2,5,-2,-5,4,2])
# truncatedTet = LCF([2,6,-2,2,6,-2,2,6,-2,2,6,-2])
# heawood = LCF([5,-5,5,-5,5,-5,5,-5,5,-5,5,-5,5,-5])

# flower = LCF([3,-3,3,-3,3,-3,3,-3,3,-3,3,-3])

# wheel = LCF([6,6,6,6,6,6,6,-6,-6,-6,-6,-6,-6,-6])

special = []


# for graph in allGraphs(8):
    
#     print(graph)
#     if graph._edge_count == 24:
#         test = Minimax(GameState(graph))

#         if test.winner()=="P1-win":
#             print("Found P1-win graph")
#             special.append(graph)




count = 10
for g in allGraphs(12):
    if g._edge_count ==36:
        print("testing graph")
        test = Minimax(GameState(g))

        if test.winner()=="P1-win":
            cycleViz(g)


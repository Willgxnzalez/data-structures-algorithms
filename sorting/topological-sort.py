class Vertex:
    def __init__(self, origin) -> None:
        self.origin = origin
        self.destVertices = []
        self.inDegree = 0

    def addDests(self, vertices):
        for v in vertices:
            v.inDegree += 1
            self.destVertices.append(v)



def topologicalSort(G: list[Vertex]):
    L = []
    for v in G:
        if v.inDegree == 0:
            L.append(v)
    
    out = []
    size = len(G)
    vertices_processed = 0
    while L:
        v = L.pop(0)
        out.append(v.origin)
        vertices_processed += 1
        for w in v.destVertices:
            w.inDegree -= 1
            if w.inDegree == 0:
                L.append(w)
    
    if vertices_processed == size:
        print("DAG:", out)
    else:
        print("Not a DAG")

A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
H = Vertex("H")

A.addDests([F, E])
B.addDests([A, C])
C.addDests([A])
D.addDests([E, A, C])
F.addDests([E])
#E.addDests([E])
H.addDests([F, A, B])


G = [A,B,C,D,E,F,H]
 
topologicalSort(G)
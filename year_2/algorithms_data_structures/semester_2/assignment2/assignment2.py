#APQ classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Element class definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Element:
    def __init__(self,k,v,i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self,other):
        return self._key == other._key

    def __lt__(self,other):
        return self._key < other._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

    def __str__(self):
        return str((self._key,self._value,self._index))

#APQHeap class definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class APQHeap:
    def __init__(self):
        self._body = []
        self._next = 0

    def add(self,key,item):
        new = Element(key,item,self._next)
        self._body.append(new)
        self._bubbleup(self._next)
        self._next += 1
        return new

    def _bubbleup(self,i):
        parent = (i-1)//2
        #print("BODY:",self._body)
        print(self._body[i], self._body[parent])
        if parent >= 0 and self._body[i] < self._body[parent]:
            self._body[parent], self._body[i] = self._body[i], self._body[parent]
            self._body[parent]._index = parent
            self._body[i]._index = i
            self._bubbleup(parent)

    def min(self):
        if len(self._body) == 0:
            return None
        return self._body[0]

    def remove_min(self):
        if len(self._body) == 0:
            return None
        else:
            if len(self._body) > 1:
                self._body[0], self._body[self._next-1] = self._body[self._next-1], self._body[0]
                self._body[0]._index = 0
                mini = self._body.pop()
                self._next -= 1
                self._bubbledown(0)
            elif len(self._body) == 1:
                mini = self._body.pop()
                self._next -= 1
        return mini._key, mini._value

    def _bubbledown(self,i):
        left = (2*i)+1
        right = (2*i)+2
        if left < self._next-1 and right <= self._next-1:
            if self._body[left] < self._body[right] and self._body[left] < self._body[i]:
                self._body[i], self._body[left] = self._body[left], self._body[i]
                self._body[i]._index = i
                self._body[left]._index = left
                self._bubbledown(left)
            elif self._body[right] < self._body[left] and self._body[right] < self._body[i]:
                self._body[i], self._body[right] = self._body[right], self._body[i]
                self._body[i]._index = i
                self._body[right]._index = right
                self._bubbledown(right)
        elif left <= self._next-1 and self._body[left] < self._body[i]:
            self._body[i], self._body[left] = self._body[left], self._body[i]
            self._body[i]._index = i
            self._body[left] = left
            self._bubbledown(left)
                    
        
    def is_empty(self):
        if len(self._body) == 0:
            return True
        return False
        
    def update_key(self,element,newkey):
        element._key = newkey
        self._rebalance(element._index)

    def _rebalance(self,i):
        self._bubbleup(i)
        self._bubbledown(i)
        
    def get_key(self,element):
        return element._key
        
    def remove(self,element):
        if self._body[element._index] == self._body[self._next-1]:
            elmt = self._body[element._index].pop()
        else:
            self._body[element._index], self._body[self._next-1] = self._body[self._next-1], self._body[element._index]
            self._body[element._index]._index = element._index
            elmt = self._body.pop()
            self._rebalance(element._index)
        return elmt

    def length(self):
        return len(self._body)

    def __str__(self):
        result = "["
        for i in range(len(self._body)):
            if i == 0:
                result += str(self._body[i])
            else:
                result += "," + str(self._body[i])
        result += "]"
        return result
    
################################################################################
    
#Graph classes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#Vertex class definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
class Vertex:

    def __init__(self,label):
        self._label = label

    def get_label(self):
        return self._label

    def set_label(self,label):
        self._label = label

    label = property(get_label,set_label)

    def __str__(self):
        return str(self._label)

    def __lt__(self,other):
        return self._label < other.label

#Edge class definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
class Edge:
    
    def __init__(self,v1,v2,label):
        self._vertices = (v1,v2)
        self._label = label

    def first(self):
        return self._vertices[0]

    def second(self):
        return self._vertices[1]

    def get_vertices(self):
        return self._vertices

    def set_vertices(self,v1,v2):
        self._vertices = (v1,v2)
    
    def opposite(self,x):
        if x == self._vertices[0]:
            return self._vertices[1]
        elif x == self._vertices[1]:
            return self._vertices[0]
        else:
            return None

    def label(self):
        return self._label

    vertices = property(get_vertices,set_vertices)

    def __str__(self):
        return "(" + str(self._vertices[0]) + "," + str(self._vertices[1]) + ")"
        
#Graph class definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Graph:

    def __init__(self):
        self._map = {}

#graph description methods~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    def vertices(self):
        #returns a list of all vertices
        v_list = []
        for v in self._map:
            v_list.append(v)
        return v_list
        
    def edges(self):
        #returns a list of all edges
        e_list = []
        for v in self._map:
            for e in self._map[v]:
                e_list.append(self._map[v][e])
        return list(set(e_list))
        
    def num_vertices(self):
        #returns the number of vertices
        v_list = self.vertices()
        return len(v_list)
        
    def num_edges(self):
        #return the number of edges"""
        e_list = self.edges()
        return len(e_list)

    def highest_deg_v(self):
        #returns the vertex with highest degree
        high = -1
        hdv = None
        for v in self._map:
            deg = self.degree(v)
            if deg > high:
                high = deg
                hdv = v
        return hdv

    def depthfirstsearch(self,v):
        search_tree = {v:None}
        self._depthfirstsearch(v,search_tree)
        return search_tree

    def _depthfirstsearch(self,v,search_tree):
        for e in self.get_edges(v):
            opp = e.opposite(v)
            if not opp in search_tree:
                search_tree[opp] = e
                self._depthfirstsearch(opp,search_tree)

    def breadthfirstsearch(self,v):
        search_tree = {v:None}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in search_tree:
                        search_tree[x] = e
                        nextlevel.append(x)
            level = nextlevel
        return search_tree

        
#graph modification methods~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    def get_edge(self,x,y):
        #return the edge between vertex x and vertex y
        if x in self._map and self._map[x]:
            return self._map[x][y]
        
    def degree(self,x):
        #return the degree of vertex x
        if x in self._map:
            return len(self._map[x])
        
    def get_edges(self,x):
        #return a list of all edges incident on x
        if x in self._map:
            edge_lst = []
            for y in self._map[x]:
                edge = self.get_edge(x,y)
                edge_lst.append(edge)
            return edge_lst
        return None
                                      
    def add_vertex(self,label):
        #add a vertex with element elt
        new_vertex = Vertex(label)
        self._map[new_vertex] = {}
        return new_vertex

    def add_vertex_if_new(self,label):
        if len(self._map) > 0:
            for v in self._map:
                if v.label == label:
                    return v
        return self.add_vertex(label)

        
    def add_edge(self,v1,v2,label):
        #add an edge, incident in vertices x and y, with label elt
        if not v1 in self._map or not v2 in self._map:
            print("Vertex/vertices do not exist(s)!")
            return None
        new_edge = Edge(v1,v2,label)
        self._map[v1].update({v2:new_edge})
        self._map[v2].update({v1:new_edge})
        return new_edge

    def get_vertex(self,label):
        for v in self._map:
            if v.label == label:
                return v
        
    def remove_vertex(self,x):
        #remove vertex with label x and all incident edges
        if x in self._map:
            for e in self._map[x]:
                del self._map[e][x]
            del self._map[x]
        
    #def remove_edge(self,elt):
        #remove edge with label elt

#Dijkstra Shortest Path~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def dijkstra_all_apq_heap(self, s, heap = True):
        """ Return table of shortest paths from s to all reachable vertices.

            The dictionary has vertices as keys, and as values it has the
            for each v the cost of the path to get to v from s, and the last
            vertex visited before v in the path.

            This version uses an adaptable priority queue using a heap by
            default, or uses an unsorted list.
        """
        closed = {}     #dictionary of cost,path pairs for each v
        locations = {}  #dictionary of open vertex elements, for accessing APQ

        if heap:
            pq = APQHeap()  #the (heap) APQ of non-closed v
        else:
            pq = APQUnsorted()  #the (list) APQ of non-closed v

        pred = {}          #dictionary of current predecessor of each v
        pred[s] = None
        locations[s] = pq.add(0,s)        #add source as first open vertex

        while pq.length() > 0:
            cv, mcov = pq.remove_min()   #we now close vertex mcov
            print('closing', mcov, 'with cost', cv)
            del locations[mcov]
            closed[mcov] = (cv, pred[mcov]) #store true cost and predecessor
            for e in self.get_edges(mcov):
                w = e.opposite(mcov)
                print('  edge to', w, end = ' ')
                if w not in closed:
                    weight = e.label()
                    newcost = cv + weight
                    if w not in locations:
                        pred[w] = mcov
                        print(' - found path to', w, 'with cost', newcost)
                        locations[w] = pq.add(newcost,w)
                    elif newcost < pq.get_key(locations[w]):    #found cheaper path to w
                        pred[w] = mcov
                        print(' - found NEW path to', w, 'with cost', newcost)
                        pq.update_key(locations[w], newcost)
                    else:
                        print(' - no improvement')
                else:
                    print(' - already closed')

        return closed
  
    def __str__(self):
        string = "{"
        j = 0
        for v in self._map:
            string += str(v) + ":{"
            i = 0
            for e in self._map[v]:
                if i%2 != 0:
                    string += "," + str(e) + ":" + str(self._map[v][e])
                else:
                    string += str(e) + ":" + str(self._map[v][e]) 
                i += 1
            j += 1
            if j == len(self._map):
                string += "}"
            else:
                string += "},"
        string += "}"
        return string

#lab 4 graph/processing methods~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
def read_dolphin_graph():
    graph = Graph()
    file = open('dolphins.gml', 'r')
    names = dict()
    file.readline() #the header with author details
    file.readline() #the start of the graph
    file.readline() #the opening square bracket
    file.readline() #the comment that the graph is not directed
    wordlist = file.readline().split()
    while wordlist[0] != ']':
        if wordlist[0] == 'node':
            file.readline() #open bracket
            nodeid = int(file.readline().split()[1])
            vertex = graph.add_vertex(nodeid)
            names[nodeid] = file.readline().split()[1]
            #print('added vertex', vertex, 'with label', names[nodeid])
            file.readline() #close bracket
        elif wordlist[0] == 'edge':
            file.readline() #open bracket
            source = int(file.readline().split()[1])
            target = int(file.readline().split()[1])
            sv = graph.get_vertex(source)
            tv = graph.get_vertex(target)
            edge = graph.add_edge(sv, tv, 1)
            #print('added edge, source =', source, '; target =', target, ':', edge)
            file.readline()
        else:
            print('ERROR: unrecognised line:', line)
        wordlist = file.readline().split()
    return graph,names

def process_dolphins():
    graph,names = read_dolphin_graph()
    print('Graph has', graph.num_vertices(), 'vertices.')
    print('Graph has', graph.num_edges(), 'edges.')
    hdv = graph.highest_deg_v()
    print(hdv.label,
          '(', names[hdv.label], ')' 
          'has the highest degree =',
          graph.degree(hdv))
    print(graph)
    print(names)
    for v in sorted(graph.vertices()):
        print(v, names[v.label], '; deg =', graph.degree(v))
    
def read_usa_graph():
    graph = Graph()
    file = open("contiguous-usa.dat","r")
    count = 1
    for line in file:
        pair = line.split()
        state1 = pair[0]
        state2 = pair[1]
        v1 = graph.add_vertex_if_new(state1)
        v2 = graph.add_vertex_if_new(state2)
        graph.add_edge(v1,v2,count)
        count += 1
    file.close()
    return graph

def process_usa_graph():
    graph = read_usa_graph()
    print(graph.highest_deg_v())

###############################################################################
#graph reader~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph

#test block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    
if __name__ == "__main__":
    """v1 = Vertex("a")
    v2 = Vertex("b")
    print("v1 label(): ",v1.label)
    print("v2 label(): ",v2.label)
    print("__str__v1: ",v1)
    print("__str__v2: ",v2)

    print()

    e1 = Edge(v1,v2,"1")
    print("edge v1: ",e1.first())
    print("edge v2: ",e1.second())
    print("vertices: ",e1.vertices)
    print("opposite v1: ",e1.opposite(v1))
    print("opposite v2: ",e1.opposite(v2))
    print("label: ",e1.label())
    print("__str__: ",e1)

    print()

    g1 = Graph()
    x = g1.add_vertex("x")
    #print("vertex ",x)
    y = g1.add_vertex("y")
    #print("vertex ",y)
    z = g1.add_vertex("z")
    #print("vertex ",z)
    A = g1.add_edge(x,y,"A")
    #print("edge ",A)
    B = g1.add_edge(x,z,"B")
    #print("edge ",B)
    print(g1)
    #print(g1.vertices())
    #print(g1.edges())
    st = g1.depthfirstsearch(x)
    for item in st:
        print(item,":",st[item])
    g1.remove_vertex(y)
    print("after removed y")
    
    print(g1._map)
    lst = g1.get_edges(y)
    for i in g1._map:
        print(i,g1._map[i])
    print(g1.vertices())
    print(g1.edges())

    #print(read_usa_graph())
    #process_usa_graph()
    #print(read_dolphin_graph())
    process_dolphins()"""

    g = graphreader("simplegraph1.txt")
    s = g.get_vertex(1)
    g.dijkstra_all_apq_heap(s)

    g = graphreader("simplegraph2.txt")
    s = g.get_vertex(1)
    short = g.dijkstra_all_apq_heap(s)
    print(short)
    
    

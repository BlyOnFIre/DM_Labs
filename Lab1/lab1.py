import sys
import re

# Initialize parent and rank dictionaries for disjoint set operations
parent = dict()
rank = dict()


# Function to open the input file
def open_file():
    try:
        return open("l1_3.txt")
    except FileNotFoundError:
        print("Oops! File not exist...")
        exit()

    file_name = sys.argv[1]
    try:
        return open(file_name)
    except FileNotFoundError:
        print("Oops! File not exist...")
        exit()


# Function to create a set for a given vertice
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


# Function to find the root of a vertice
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


# Function to merge two sets containing vertice1 and vertice2
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


# Function to perform Kruskal's algorithm on a given graph
def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


# Open the input file
file = open_file()

# Read the size of the graph and create a list of vertices
size = int(file.readline())
vertices = []
for i in range(size):
    vertices.append(i)

# Initialize the matrix and edges list
matrix = dict()
edges = []

# Read the input file and store the edges in the edges list
for line_index, line in enumerate(file):
    nodes = list(filter(None, re.split(r'\s', re.sub('\n', '', line))))
    for index, node in enumerate(nodes):
        if line_index == index or node == '0' or (str(index) + ',' + str(line_index)) in matrix: continue
        matrix[str(line_index) + ',' + str(index)] = 1
        edges.append((int(node), line_index, index))

# Create the graph with vertices and edges
graph = {'vertices': vertices, 'edges': set(edges)}

# Find the minimum spanning tree using Kruskal's algorithm
min_spanning_tree = sorted(kruskal(graph))

# Print the minimum spanning tree and its total weight
print("Minimum spanning tree:")
tree_weight = 0
for node in min_spanning_tree:
    tree_weight += node[0]
    print(str(node[1]) + '->' + str(node[2]) + '(' + str(node[0]) + ')', end='; ')

print("\nWeight of the minimum spanning tree:", tree_weight)

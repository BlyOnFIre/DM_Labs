import sys
import re

# Initialize parent and rank dictionaries for disjoint set operations
parent = dict()
rank = dict()

# Function to open the input file
def open_file(file_name):
    try:
        return open(file_name)
    except FileNotFoundError:
        print("Oops! File not exist...")
        sys.exit()

# Function to create a set for a given vertex
def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

# Function to find the root of a vertex
def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

# Function to merge two sets containing vertex1 and vertex2
def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

# Function to perform Boruvka's algorithm on a given graph
def boruvka(graph):
    for vertex in graph['vertices']:
        make_set(vertex)

    min_spanning_tree = set()
    num_of_components = len(graph['vertices'])

    while num_of_components > 1:
        cheapest = [-1] * len(graph['vertices'])
        for edge in graph['edges']:
            weight, vertex1, vertex2 = edge
            root1 = find(vertex1)
            root2 = find(vertex2)
            if root1 != root2:
                if cheapest[root1] == -1 or weight < cheapest[root1][0]:
                    cheapest[root1] = edge
                if cheapest[root2] == -1 or weight < cheapest[root2][0]:
                    cheapest[root2] = edge

        for edge in cheapest:
            if edge != -1:
                weight, vertex1, vertex2 = edge
                root1 = find(vertex1)
                root2 = find(vertex2)
                if root1 != root2:
                    union(vertex1, vertex2)
                    min_spanning_tree.add((weight, vertex1, vertex2))
                    num_of_components -= 1

    return min_spanning_tree


# Read the input file
file_name = "l1_3.txt"
file = open_file(file_name)

# Read the size of the graph and create a list of vertices
size = int(file.readline())
vertices = [i for i in range(size)]

# Read the input file and store the edges in the edges list
edges = []
for line_index, line in enumerate(file):
    nodes = list(filter(None, re.split(r'\s', re.sub('\n', '', line))))
    for index, node in enumerate(nodes):
        if line_index == index or node == '0' or (line_index, index) in edges: continue
        edges.append((int(node), line_index, index))

# Create the graph with vertices and edges
graph = {'vertices': vertices, 'edges': set(edges)}

# Find the minimum spanning tree using Boruvka's algorithm
min_spanning_tree = sorted(boruvka(graph))

# Print the minimum spanning tree and its total weight
print("Minimum spanning tree:")
tree_weight = 0
for edge in min_spanning_tree:
    tree_weight += edge[0]
    print(f"{edge[1]}->{edge[2]}({edge[0]})", end="; ")

print("\nWeight of the minimum spanning tree:", tree_weight)
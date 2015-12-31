#!/usr/bin/env python3

import networkx as nx
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file with the adjacency list", type=str)
    args = parser.parse_args()
    input_file = args.input

    # Load graph from adjacency list
    G = nx.read_adjlist(input_file)

    print("\nDiameter: %d" % nx.diameter(G))
    print("\nAverage shortest path: %.4f" % nx.average_shortest_path_length(G))
    print("\nAverage clustering: %.4f" % nx.average_clustering(G))
    print("\nEfficiency of the network: %.4f" % efficiency(G))

    clustDict = nx.clustering(G)
    print("\nClustering for each node:")
    for n in sorted(clustDict, key=int):
        print("\tNode %s: %.4f" % (n, clustDict[n]))

    degreeDict = nx.degree(G)
    print("\nNode degrees:")
    for n in sorted(degreeDict, key=int):
        print("\tNode %s: %d" % (n, degreeDict[n]))

    closenessDict = nx.closeness_centrality(G)
    print("\nCloseness centrality of nodes:")
    for n in sorted(closenessDict, key=int):
        print("\tNode %s: %.4f" % (n, closenessDict[n]))

    beetwennessDict = nx.betweenness_centrality(G, normalized=False)
    print("\nBetweenness centrality of nodes (not normalized):")
    for n in sorted(beetwennessDict, key=int):
        print("\tNode %s: %.4f" % (n, beetwennessDict[n]))

    coreDict = nx.core_number(G)
    print("\nk-core decomposition for each node:")
    for n in sorted(coreDict, key=int):
        print("\tNode %s: %d-core" % (n, coreDict[n]))

# Source: https://networkx.lanl.gov/trac/ticket/611#comment:2
def efficiency(G):
    avg = 0.0
    n = len(G)
    for node in G:
        path_length = nx.single_source_shortest_path_length(G, node)
        avg += sum(1.0/v for v in path_length.values() if v !=0)
    avg *= 1.0/(n*(n-1))
    return avg

if __name__ == "__main__":
    main()

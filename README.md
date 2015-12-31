# csr_networkx

## Scope

This is a Python script to perform a basic graph analysis on simple, undirected graphs.

The original aim of this script is to quickly generate solutions for the exercises of the [Network complexity course](http://home.deib.polimi.it/piccardi/csr.html) taught in Politecnico di Milano by prof. Carlo Piccardi.

The script computes the following metrics:
* Diameter of the network
* Average distance
* Clustering coefficient (global and local)
* Efficiency of the network
* Degree of each node
* Closeness centrality
* Betweenness centrality
* k-core decomposition of nodes

## Installation and requirements

This script requires [Python 3](https://www.python.org/download/releases/3.0/) and the [NetworkX](https://networkx.github.io/) package.

If you have already installed Python 3, you can install NetworkX with [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)):

    pip3 install networkx

## Usage

To use the script, you'll need to provide a graph in a file as an adjacency list.
See the [reference of the package](http://networkx.github.io/documentation/latest/reference/readwrite.adjlist.html) for the syntax and the `20150204_es5.txt` file for an example.

Usage:

    python3 analyze.py <input_file>

Example:

    python3 analyze.py 20150204_es5.txt

Sample output:

    $ python3 analyze.py 20150204_es5.txt

    Diameter: 4

    Average shortest path: 2.3485

    Average clustering: 0.5694

    Efficiency of the network: 0.5518

    Clustering for each node:
    	Node 1: 0.6667
    	Node 2: 0.3333
    	Node 3: 0.6667
    	Node 4: 0.3333
    	Node 5: 1.0000
    	Node 6: 0.3333
    	Node 7: 0.3333
    	Node 8: 1.0000
    	Node 9: 0.5000
    	Node 10: 0.6667
    	Node 11: 0.6667
    	Node 12: 0.3333

    Node degrees:
    	Node 1: 3
    	Node 2: 3
    	Node 3: 3
    	Node 4: 3
    	Node 5: 2
    	Node 6: 3
    	Node 7: 3
    	Node 8: 3
    	Node 9: 4
    	Node 10: 4
    	Node 11: 4
    	Node 12: 3

    Closeness centrality of nodes:
    	Node 1: 0.4231
    	Node 2: 0.4074
    	Node 3: 0.4231
    	Node 4: 0.4400
    	Node 5: 0.3667
    	Node 6: 0.4231
    	Node 7: 0.4400
    	Node 8: 0.3929
    	Node 9: 0.4583
    	Node 10: 0.4583
    	Node 11: 0.4583
    	Node 12: 0.4400

    Betweenness centrality of nodes (not normalized):
    	Node 1: 3.6667
    	Node 2: 9.6667
    	Node 3: 3.6667
    	Node 4: 13.1667
    	Node 5: 0.0000
    	Node 6: 9.8333
    	Node 7: 11.8333
    	Node 8: 0.0000
    	Node 9: 14.1667
    	Node 10: 5.1667
    	Node 11: 5.1667
    	Node 12: 12.6667

    k-core decomposition for each node:
    	Node 1: 2-core
    	Node 2: 2-core
    	Node 3: 2-core
    	Node 4: 2-core
    	Node 5: 2-core
    	Node 6: 2-core
    	Node 7: 2-core
    	Node 8: 3-core
    	Node 9: 3-core
    	Node 10: 3-core
    	Node 11: 3-core
    	Node 12: 2-core

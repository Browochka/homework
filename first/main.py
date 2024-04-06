import networkx as nx
import matplotlib.pyplot as plt


TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_wo_cycles.edgelist",
    "graph_3_w_cycles.edgelist",

]

def has_cycles(g: nx.DiGraph):
    try:
        t = nx.find_cycle(g, orientation='original')
        return True
    except:
        return False


if __name__ == "__main__":
    for filename in TEST_GRAPH_FILES:
        # Load the graph
        G = nx.read_edgelist(f"{filename}", create_using=nx.DiGraph)
        # Output whether it has cycles
        print(f"Graph {filename} has cycles: {has_cycles(G)}")

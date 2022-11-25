import matplotlib.pyplot as plt
import networkx as nx


# create a directed multi-graph
multiplier = 50
minVerCount = 5*multiplier
minColoredCount = 1*multiplier

G = nx.MultiDiGraph()
G = nx.erdos_renyi_graph (minVerCount,0.02)
rad = 1
colors = ['r','b','y','c','g']*minColoredCount


plt.figure(figsize=(20,10)) # plotting a frame
nx.draw(G, connectionstyle=f'arc3, rad = {rad}', with_labels = False, node_size=50, node_color=colors) # plotting the graph
plt.show()  # pause before exiting


G.clear()
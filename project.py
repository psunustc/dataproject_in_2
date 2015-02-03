from operator import itemgetter
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

fpath = '/Users/pengsun/Documents/bigdata/incubator/20150128/Amazon0302.txt'
infile = open(fpath, 'r')
head_lines = 4

for n, line in enumerate(infile):
    if n > head_lines:
        tmp = line.split()
        G.add_edge( int(tmp[0]), int(tmp[1]) )
        
infile.close()

node_and_degree=G.degree()
(largest_hub,degree)=sorted(node_and_degree.items(),key=itemgetter(1))[-1]

hub_ego = nx.ego_graph(G, largest_hub, undirected=True)
pos=nx.spring_layout(hub_ego)
#nx.draw(hub_ego,pos,node_color='b',node_size=50,with_labels=False)
    # Draw ego as large and red
#nx.draw_networkx_nodes(hub_ego,pos,nodelist=[largest_hub],node_size=300,node_color='r')

#plt.savefig('ego_graph.png')
#plt.show()

dlist = nx.degree_histogram(G)
dlist = dlist*1.0/sum(dlist)
plt.loglog(dlist)
plt.xlabel('Degrees of nodes')
plt.ylabel('Number of nodes')
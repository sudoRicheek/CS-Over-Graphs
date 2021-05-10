import snap
import math
import igraph
import numpy as np
from lasso import lasso
from numpy.random import default_rng

rng = default_rng()

graph = snap.LoadEdgeList(snap.TUNGraph, "facebook_combined.txt", 0, 1)

print("Nodes and Edges: (",graph.GetNodes(), graph.GetEdges(),")")

n = graph.GetNodes()

k = 1  # Parameter
k1 = 2*k

epsilon = 0.15  # \in (0,1/6)
theta = 0.1  # \in [0,1)
mu = 0.95  # >0
C = 2  # >1

d = (1/epsilon) * (np.log(np.e * (theta+1) * n)/np.log(mu * C))
m = (1/epsilon) * C * d * k1

d = math.ceil(d)
m = math.ceil(m)
print("d: ",d)
print("m: ",m)

scoreMat = np.zeros((n, 1))
A = np.zeros((m, n))

########################
#MAKE MEASUREMENT MATRIX
########################
for j in range(n):  # 0 ... n-1
    # Select d numbers without replacement from 0 ... m-1
    row = rng.choice(m, size=d, replace=False)
    A[row, j] = 1
# Measurement matrix constructed

######################################################################
#FIND THE LOCAL BETWEENESS VALUES(Global betweenness is not tractable)
######################################################################
for u in graph.Nodes():
    v = u.GetId()
    num_nbrs, nbrs = graph.GetNodesAtHop(v, 1, False)
    nbrs.insert(0, v)
    egoadj = np.zeros((len(nbrs), len(nbrs)))
    for i, v1 in enumerate(nbrs):
        for j, v2 in enumerate(nbrs):
            if v1 != v2:
                egoadj[i, j] = 1 if graph.IsEdge(
                    v1, v2) or graph.IsEdge(v2, v1) else 0
    adj2 = np.dot(egoadj, egoadj)
    score = 0
    for (x, y), value in np.ndenumerate(egoadj):
        # 1-egoAdj comes from the value==0 condition
        if x < y and value == 0 and adj2[x, y] != 0:
            score = score + 1 / (adj2[x, y])
    scoreMat[v] = score
scoreMat = scoreMat/np.linalg.norm(scoreMat) # Normalize the scores

#########################
# GET THE MEASURED MATRIX
#########################
y = np.zeros((m,1)) # This is the matrix we get as measured in real life
for i in range(m):
    y[i] = A[i,:].dot(scoreMat)

print("True Local Betweenness Values: ")
print(scoreMat)
print()
#####################
# SOLVE LASSO PROBLEM
#####################
x = lasso(A, y)

print("Reconstructed Local Betweenness Values: ")
print(x)

###############################
#CALCULATE RECONSTRUCTION ERROR
###############################
MSE = np.linalg.norm(scoreMat-x)
print("Relative L2-Norm Error Percentage: ", 100*MSE, "%")
# print(np.linalg.norm(scoreMat)) # This is ofc 1

#################
#PLOTTING UTILITY
#################
g = igraph.Graph([(e.GetSrcNId(),e.GetDstNId()) for e in graph.Edges()])
g.vs["loc_btwness"] = x.flatten()
layout = g.layout("lgl")

##########################
# PARAMETER FOR CHANGING K
##########################
topk=10
visual_style = {}
visual_style["vertex_size"] = [10*wt for wt in g.vs["loc_btwness"]]
visual_style["edge_width"] = 0.1
visual_style["layout"] = layout
visual_style["bbox"] = (800,800)
visual_style["edge_color"] = "DodgerBlue"

idxTopK = np.argpartition(g.vs["loc_btwness"], -topk)[-topk:]  # Indices not sorted
print("Top ",topk," information flow hotspots(RECONSTRUCTED): ", np.sort(idxTopK))
realTopK = np.argpartition(scoreMat.flatten(), -topk)[-topk:]  # Indices not sorted
print("Top ",topk," information flow hotspots(TRUE): ", np.sort(realTopK))

visual_style["vertex_label"] = [node if node in idxTopK else None for node, val in enumerate(g.vs["loc_btwness"])]

visual_style["vertex_label_dist"] = 0
visual_style["vertex_label_angle"] = 0.1
igraph.plot(g, **visual_style)

################################
## Uncomment to store the plots#
################################

# visual_style["bbox"] = (4000,4000)
# visual_style["vertex_size"] = [100*wt for wt in g.vs["loc_btwness"]]
# visual_style["vertex_label_size"] = 50
# igraph.plot(g,target="facebookTop"+str(topk)+".png",**visual_style)
# igraph.plot(g,target="facebookTop"+str(topk)+".pdf",**visual_style)
import sys
import snap
import math
import numpy as np
from csv import writer
from lasso import lasso
from numpy.random import default_rng

if len(sys.argv) != 5:
    print("USAGE: python3 tabulate_performance_fb.py <d> <m> <topk> <csvfile>")
    exit(1)

rng = default_rng()

graph = snap.LoadEdgeList(snap.TUNGraph, "facebook_combined.txt", 0, 1)

# print("Nodes and Edges: (",graph.GetNodes(), graph.GetEdges(),")")

n = graph.GetNodes()

d = int(sys.argv[1])
m = int(sys.argv[2])
print("d: ", d)
print("m: ", m)

scoreMat = np.zeros((n, 1))
A = np.zeros((m, n))

########################
# MAKE MEASUREMENT MATRIX
########################
for j in range(n):  # 0 ... n-1
    # Select d numbers without replacement from 0 ... m-1
    row = rng.choice(m, size=d, replace=False)
    A[row, j] = 1
# Measurement matrix constructed

######################################################################
# FIND THE LOCAL BETWEENESS VALUES(Global betweenness is not tractable)
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
scoreMat = scoreMat/np.linalg.norm(scoreMat)  # Normalize the scores

#########################
# GET THE MEASURED MATRIX
#########################
y = np.zeros((m, 1))  # This is the matrix we get as measured in real life
for i in range(m):
    y[i] = A[i, :].dot(scoreMat)

#####################
# SOLVE LASSO PROBLEM
#####################
x = lasso(A, y)

###############################
# CALCULATE RECONSTRUCTION ERROR
###############################
MSE = np.linalg.norm(scoreMat-x)
print("Relative L2-Norm Error Percentage: ", 100*MSE, "%")
# print(np.linalg.norm(scoreMat)) # This is ofc 1

##########################
# PARAMETER FOR CHANGING K
##########################
topk = 200  # Change this to get the topK information flow hotspots
topk = int(sys.argv[3])

idxTopK = np.argpartition(x.flatten(), -topk)[-topk:]  # Indices not sorted
idxTopK = np.sort(idxTopK)
realTopK = np.argpartition(
    scoreMat.flatten(), -topk)[-topk:]  # Indices not sorted
realTopK = np.sort(realTopK)

CATERROR = topk - np.size(np.intersect1d(idxTopK, realTopK))
print("Categorization Error: ", CATERROR, " mismatches")


# Row which we want to append to our error csv file
OutputList = [d, m, topk, 100*MSE, CATERROR]
with open(sys.argv[4], 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(OutputList)
    f_object.close()

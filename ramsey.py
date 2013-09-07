from numpy import *
import networkx as nx
import matplotlib.pyplot as plt
import random 




rowcount=0
numberOfGraphs=1
numberOfNodes=43

testMatrix=zeros((numberOfGraphs,numberOfNodes,numberOfNodes), dtype=bool)




for x in nditer(testMatrix, op_flags=['readwrite']):
    x[...] = bool(random.getrandbits(1))



for i in range(numberOfGraphs):
    fill_diagonal(testMatrix[i], 0)
    
for i in range(numberOfGraphs):
    for j in range(numberOfNodes):
        for k in range(numberOfNodes):
            x=testMatrix[i][j][k]
            testMatrix[i][k][j]=x


k5total=0
otherK5Total=0
numberOfK5=0

for i in range(numberOfGraphs):
    for aa in range(numberOfNodes-4):
        for ab in range(aa,numberOfNodes-3):
            if testMatrix[i][aa][ab]==1:
                for ac in range(ab,numberOfNodes-2):
                    if testMatrix[i][aa][ac]==1 & testMatrix[i][ab][ac]==1:
                        for ad in range(ac,numberOfNodes-1):
                            if testMatrix[i][aa][ad]==1 & testMatrix[i][ab][ad]==1 & testMatrix[i][ac][ad]==1:
                                for ae in range(ad,numberOfNodes):
                                    if testMatrix[i][aa][ae]==1 & testMatrix[i][ab][ae]==1 & testMatrix[i][ac][ae]==1 & testMatrix[i][ad][ae]==1:
                                        k5total+=1
                                        print(i)
                                        D=nx.Graph(testMatrix[i])
                                        c=list((nx.k_clique_communities(D,5)))
                                        numberOfK5=len(c)
                                        if numberOfK5 >0:
                                            otherK5Total+=1
                                        #print(numberOfK5)
                                    
                                        #nx.draw_circular(D)
                                        #plt.show()                                    
   
    
print k5total
print otherK5Total

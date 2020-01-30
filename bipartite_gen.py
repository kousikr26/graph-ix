import random
from numpy.random import randint
import numpy as np

n=400
vertices=list(range(n))
train_graphs=400
test_graphs=50
all_graphs=[]
preds=[]
np.set_printoptions(threshold=np.inf)

for g in range(train_graphs):
	k=random.randint(1,n-1)
	first=random.sample(vertices,k)
	second=list(set(vertices)-set(first))
	adj=np.zeros((n,n))
	for i in first:
		edges=randint(0,2,len(second))
		
		for j in range(len(second)):
			if edges[j]==1:
				adj[i][second[j]]=1
				adj[second[j]][i]=1
	all_graphs.append(adj)
	preds.append(1)

c=0
for g in range(train_graphs):

	k=random.randint(1,n-1)
	first=random.sample(vertices,k)
	second=list(set(vertices)-set(first))
	adj=np.zeros((n,n))
	for i in first:
		edges=randint(0,2,len(second))
		
		for j in range(len(second)):
			if edges[j]==1:
				adj[i][second[j]]=1
				adj[second[j]][i]=1
	inter_edges=0
	for i in range(len(first)):
		edges=randint(0,2,len(first))
		for j in range(len(first)):
			if(i!=j and edges[j]==1):
				inter_edges+=1
				adj[i][j]=1
	for i in range(len(second)):
		edges=randint(0,2,len(second))
		for j in range(len(second)):
			if(i!=j and edges[j]==1):
				inter_edges+=1
				adj[i][j]=1
	
	if inter_edges>0 :
		all_graphs.append(adj)
		preds.append(0)
		c+=1
		#print(adj.tolist())
		print(inter_edges)






all_graphs=np.array(all_graphs)

preds=np.array(preds)
print(all_graphs.shape)
print(preds.shape)
np.save('x_train',all_graphs)
np.save('y_train',preds)




test_graphs=50
all_graphs=[]
preds=[]


for g in range(test_graphs):
	k=random.randint(1,n-1)
	first=random.sample(vertices,k)
	second=list(set(vertices)-set(first))
	adj=np.zeros((n,n))
	for i in first:
		edges=randint(0,2,len(second))
		
		for j in range(len(second)):
			if edges[j]==1 :
				adj[i][second[j]]=1
				adj[second[j]][i]=1
	all_graphs.append(adj)
	preds.append(1)


for g in range(test_graphs):
	k=random.randint(1,n-1)
	first=random.sample(vertices,k)
	second=list(set(vertices)-set(first))
	adj=np.zeros((n,n))
	for i in first:
		edges=randint(0,2,len(second))
		
		for j in range(len(second)):
			if edges[j]==1:
				adj[i][second[j]]=1
				adj[second[j]][i]=1
	inter_edges=0
	for i in range(len(first)):
		edges=randint(0,2,len(first))
		for j in range(len(first)):
			if(i!=j and edges[j]==1):
				inter_edges+=1
				adj[i][j]=1
	for i in range(len(second)):
		edges=randint(0,2,len(second))
		for j in range(len(second)):
			if(i!=j and edges[j]==1):
				inter_edges+=1
				adj[i][j]=1
	if inter_edges>0:
		all_graphs.append(adj)
		preds.append(0)










np.save('x_test',all_graphs)
np.save('y_test',preds)

import numpy as np
import matplotlib.pyplot as plt

class graph:
	def __init__(self,adjmat):
		self.n=adjmat.shape[0]
		self.adjmat=adjmat
		if self.adjmat.T==self.adjmat:
			self.directed=False
		countEdges()

	def countEdges(self):
		if(self.directed):
			self.m=np.sum(self.adjmat)
		else:
			self.m=np.sum(self.adjmat)/2

test=np.array([[0,0,1],
				[0,0,0],
				[1,0,0]])
testgraph=graph(test)
print(testgraph.n)
# graph-ix
Graph algorithms using deep learning
## Ongoing

# Objective

**Using Neural Networks to obtain a heuristic solution to NP-hard graph
problems.**


Since Neural Networks are basically repeated matrix products, if we
are able to train a neural network to output an approximate solution to
NP-hard graph problems we can solve the problem in polynomial time i.e
\(O(n^3)\) (\(O(n^{2.37})\) using Coppersmith-Winograd multiplication)
where \(n\) is the number of vertices in the graph as training is done
on adjacency matrix of graph

# Results

Results on training a neural network for **bipartite classification** task 

| Number of vertices(n) | NN depth | Parameters | Epochs | Test accuracy |
| :-------------------: | :------: | :--------: | :----: | :-----------: |
|          40           | 2 layers |    74k     |   10   |      96%      |
|          400          | 2 layers |    7.2M    |   10   |      97%      |

Results on bipartite classification task

  
The test was just a feasibility analysis and the process is not optimized. The results were pretty interesting and the problem could be explored on more complex graph problems especially NP hard problems
where the network would actually be able to provide an improvement in
performance over traditional algorithms.  

# Scope of Improvement

  - Use a better and more uniform method for random graph
    generation(Current naive method produces most graphs with
    \(m={n C 2}/2\))

  - Better network architecture and extension to problems other than
    classification

  - Use of Graph Convolutional Network to control the growing number of
    parameters with \(n\)

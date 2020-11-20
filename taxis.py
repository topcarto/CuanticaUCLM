from collections import defaultdict
from dimod import BinaryQuadraticModel
from dwave.system.samplers import DWaveSampler, EmbeddingComposite

Q = defaultdict(int)
for u, v, w in G.edges
    Q[(u,u)] += -1
    Q[(v,v)] += -1
    Q[(w,w)] += -1
    Q[(u,v)] += 0
    Q[(u,w)] += 1
    Q[(v,w)] += 1

bqm = BinaryQuadraticModel.from_qubo(Q)

sampler = EmbeddingComposite(DWaveSampler(solver={'qpu':True}))
sampleset = sampler.sample(bqm)

print(sampleset.first)
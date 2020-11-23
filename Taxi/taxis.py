from collections import defaultdict
from dimod import BinaryQuadraticModel
from dwave.system import LeapHybridSampler

Q = defaultdict(int)
Q[(0,0)] += -1
Q[(1,1)] += -1
Q[(2,2)] += -1
Q[(0,1)] += 0
Q[(0,2)] += 1
Q[(1,2)] += 1

bqm = BinaryQuadraticModel.from_qubo(Q)

sampler = LeapHybridSampler()
sampleset = sampler.sample(bqm)
sample = sampleset.first.sample
energy = sampleset.first.energy

print("Información: " + sampleset.info)
print("Record: " + sampleset.record)
print("Resultado final: " + sample)
print("Energía del resultado final: " + energy)
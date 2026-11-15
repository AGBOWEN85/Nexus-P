from nexus.quantum import QuantumModule

qm = QuantumModule(3)
qm.apply('h', 0)
qm.apply('cx', 0, 1)
print(qm.measure_all())

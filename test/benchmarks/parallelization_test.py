import sys
import qiskit
from qiskit import compile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.aer import QasmSimulator

#import python tools
import numpy as np
import copy
import timeit
import matplotlib.pyplot as plt
import math

from quantumvolume import quantum_volume_circuit

qubit = 10
depth = 10
measure = True
seed = 0
shots = 1024

simulator = QasmSimulator()

parallel_shots_list = { 1, 5, 10, 20, 30, 40, 50, 60, 70, 80}

circuit = quantum_volume_circuit(qubit, depth, measure, seed)
qobj = compile(circuit, simulator, shots=shots)

for parallel_shots in parallel_shots_list:
    backend_opts = { 
        'max_parallel_threads': 80,
        'max_parallel_shots': parallel_shots,
        'parallel_state_update': 80 / parallel_shots
        }
    
    result = simulator.run(qobj, backend_options=backend_opts).result()
    
    print (80, parallel_shots, 80 / parallel_shots, result.metadata['time_taken'])

import qiskit as q

def mensura_qubit(qubits: int, classical_bits: int) -> q.result.counts.Counts:

    # Usando Aer's qasm_simulator
    simulador = q.Aer.get_backend("qasm_simulator")
    # Criando um circuito quantico que atua sobre um registrador
    circuito = q.QuantumCircuit(qubits, classical_bits)
    # Mapeando os possíveis estados de um bit clássico
    circuito.measure([0], [0])

    # Executando o circuito no simulador
    executa_circuito = q.execute(circuito, simulador, shots=1000) # Experimento executado 1000 vezes
    # Retornando o histograma dos resultados do experimento
    return executa_circuito.result().get_counts(circuito)

if __name__ == "__main__":
    print(f"Total count for various states are: {mensura_qubit(1, 1)}")
    

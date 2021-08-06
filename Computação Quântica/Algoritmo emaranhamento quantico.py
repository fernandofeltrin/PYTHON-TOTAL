import qiskit

def emaranhamento(qubits: int = 2) -> qiskit.result.counts.Counts:
    """
    #      ┌───┐     ┌─┐
    # q_0: ┤ H ├──■──┤M├───
    #      └───┘┌─┴─┐└╥┘┌─┐
    # q_1: ─────┤ X ├─╫─┤M├
    #           └───┘ ║ └╥┘
    # c: 2/═══════════╩══╩═
    #                 0  1
    """
    n_bits = qubits
    # Usando Aer's qasm_simulator
    simulador = qiskit.Aer.get_backend("qasm_simulator")
    # Criando um circuito quantico que atua sobre um registrador
    circuito = qiskit.QuantumCircuit(qubits, n_bits)
    # Adicionando uma ponte H ao qubit (aplicando superposição a q0)
    circuito.h(0)

    for i in range(1, qubits):
        circuito.cx(i - 1, i) # Porta lógica quantica CNOT

    # Mapeando os possíveis estados dos bits clássicos
    circuito.measure(list(range(qubits)), list(range(n_bits)))
    # Executando o circuito
    executa_circuito = qiskit.execute(circuito, simulador, shots=1000)
    return executa_circuito.result().get_counts(circuito)

if __name__ == "__main__":
    print(f"Total de possíveis estados: {emaranhamento(3)}")

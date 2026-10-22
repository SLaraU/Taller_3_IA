"""Punto 2. Inferencia exacta por enumeración."""
from algorithms.probability import normalize


def enumeration_ask(network, query: str, evidence: dict) -> dict:
    """Calcula P(query | evidence) sobre la conjunta factorizada.

    Entradas: network es la red; query es el nombre de la
    variable consultada; evidence es {nombre de variable: 0 o 1}.
    Salida: {0: probabilidad, 1: probabilidad}.

    Tips:
    - Recorra network.variables en orden topológico.
    - Para una variable fijada multiplique su probabilidad; para una oculta
      sume las dos alternativas 0 y 1. Normalice al terminar.
    - Use copias del evento y no modifique evidence.
    - network.probability(variable, valor, evento) consulta la CPT;
      el evento debe contener los valores de todos los padres.
    - Puede usar una función auxiliar recursiva. Al terminar el recorrido,
      el producto sin factores restantes vale 1.
    - Evidencia imposible: ValueError. Consulta observada: distribución puntual
      solo si la evidencia es posible.
    """
    # Valida nombres de variables y dominio de la evidencia.
    network.validate_query(query, evidence)

    # TODO: Add your code here
    variables = network.variables

    def enumerate_all(index, event):

        # Al terminar el recorrido, el producto sin factores vale 

        if index == len(variables):
          
            return 1.0
        var = variables[index]
        if var in event:
            return network.probability(var, event[var], event) * enumerate_all(index + 1, event)
       
        total = 0.0
        for value in (0, 1):
            extended = dict(event)
            extended[var] = value
            total += network.probability(var, value, extended) * enumerate_all(index + 1, extended)
        return total

    weights = {}
    for value in (0, 1):
        event = dict(evidence)         
        if query in evidence and evidence[query] != value:
            weights[value] = 0.0       
            continue
        event[query] = value
        weights[value] = enumerate_all(0, event)

    if weights[0] + weights[1] == 0:
        raise ValueError("Evidencia imposible")
    return normalize(weights)
    # FIN DEL BLOQUE DEL ESTUDIANTE
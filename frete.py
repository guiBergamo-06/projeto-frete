"""
Módulo de cálculo de frete.

Este arquivo contém as funções principais do projeto:
- calcular_frete: calcula o valor do frete com base no peso e na distância.
- aplicar_desconto: aplica um percentual de desconto sobre um valor.
"""


def calcular_frete(peso_kg, distancia_km):
    """
    Calcula o valor do frete.

    Regra de negócio:
    - Preço por kg: R$ 2,50
    - Preço por km: R$ 0,80

    Lança ValueError se o peso ou a distância forem inválidos
    (menores ou iguais a zero, ou negativos).
    """
    if peso_kg <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    if distancia_km < 0:
        raise ValueError("A distância não pode ser negativa.")

    valor_frete = (peso_kg * 2.5) + (distancia_km * 0.8)
    return round(valor_frete, 2)


def aplicar_desconto(valor, percentual_desconto):
    """
    Aplica um desconto percentual sobre um valor.

    Regra de negócio:
    - O percentual deve estar entre 0 e 100.

    Lança ValueError se o percentual estiver fora desse intervalo.
    """
    if percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("O percentual de desconto deve estar entre 0 e 100.")

    valor_com_desconto = valor - (valor * (percentual_desconto / 100))
    return round(valor_com_desconto, 2)

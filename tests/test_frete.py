"""
Testes automatizados das funções do módulo frete.py

Total de testes: 6
- 3 testes de casos válidos
- 3 testes de casos inválidos (exceções)
"""

import pytest
from frete import calcular_frete, aplicar_desconto


# ---------- Testes da função calcular_frete ----------

def test_calcular_frete_com_valores_validos():
    resultado = calcular_frete(10, 100)
    # 10kg * 2.5 = 25 / 100km * 0.8 = 80 / total = 105
    assert resultado == 105.0


def test_calcular_frete_com_peso_invalido_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete(0, 50)


def test_calcular_frete_com_distancia_negativa_gera_erro():
    with pytest.raises(ValueError):
        calcular_frete(5, -10)


# ---------- Testes da função aplicar_desconto ----------

def test_aplicar_desconto_com_valor_valido():
    resultado = aplicar_desconto(200, 10)
    assert resultado == 180.0


def test_aplicar_desconto_sem_desconto():
    resultado = aplicar_desconto(150, 0)
    assert resultado == 150.0


def test_aplicar_desconto_com_percentual_invalido_gera_erro():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)

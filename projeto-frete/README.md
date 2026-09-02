# Projeto Cálculo de Frete

## Objetivo
Este projeto foi desenvolvido para praticar testes automatizados com **Pytest** e integração contínua com **GitHub Actions**. Ele simula o cálculo de frete de uma entrega, com base no peso e na distância, além da aplicação de um desconto sobre o valor final.

## Funções implementadas

- **`calcular_frete(peso_kg, distancia_km)`**: calcula o valor do frete com base no peso (R$ 2,50 por kg) e na distância (R$ 0,80 por km). Lança um erro (`ValueError`) se o peso for menor ou igual a zero, ou se a distância for negativa.

- **`aplicar_desconto(valor, percentual_desconto)`**: aplica um percentual de desconto sobre um valor. Lança um erro (`ValueError`) se o percentual informado não estiver entre 0 e 100.

## Testes

Foram desenvolvidos **6 casos de teste**, localizados no diretório `tests/`, cobrindo:

- 3 cenários válidos (verificando o retorno correto das funções);
- 3 cenários inválidos (verificando se as exceções são lançadas corretamente, usando `pytest.raises`).

### Como executar os testes localmente

```bash
pip install -r requirements.txt
pytest -v
```

## GitHub Actions

Este repositório possui um workflow configurado em `.github/workflows/tests.yml`, que executa os testes automaticamente a cada `push` na branch `main`. O workflow:

1. Baixa o código do repositório;
2. Configura o ambiente Python;
3. Instala as dependências (`requirements.txt`);
4. Executa os testes com `pytest`;
5. Mostra na aba **Actions** se os testes passaram ou falharam.

### O que acontece se um teste falhar?

Se algum teste falhar durante a execução do GitHub Actions, o workflow é marcado com um **X vermelho** (falha) na aba Actions, em vez do check verde de sucesso. O log da execução mostra exatamente qual teste falhou e por qual motivo (a mensagem de erro do `assert` ou da exceção esperada), permitindo identificar e corrigir o problema antes de enviar uma nova versão do código.

### Resultado obtido

Após a configuração, todos os testes foram executados com sucesso na aba Actions do GitHub (ver captura de tela em anexo na entrega da atividade).

# Cálculo de Classificação de Soja

## Descrição
Este programa em Python é projetado para calcular o desconto aplicável sobre o peso líquido da soja com base em vários critérios de qualidade, como umidade, impurezas, grãos avariados, esverdeados e quebrados ou amassados.

## Funcionalidades
- **Calcula o Peso Líquido**: Determina o peso líquido da soja subtraindo a tara do peso bruto.
- **Calcula Descontos Individuais**: Calcula os descontos com base nos limites estabelecidos para umidade, impurezas, grãos avariados, esverdeados e quebrados ou amassados.
- **Calcula Desconto Total e Peso Líquido com Desconto**: Soma todos os descontos individuais para encontrar o desconto total e subtrai do peso líquido para obter o peso final após descontos.

## Como usar
1. **Defina os Dados de Entrada**: Inclua informações como peso bruto, tara e os percentuais de umidade, impurezas, grãos avariados, esverdeados, e quebrados ou amassados.
2. **Execute o Programa**: O programa processará esses dados para calcular o peso líquido e os descontos aplicáveis.

## Limites Estabelecidos para Descontos
- Umidade: 14%
- Impurezas: 1%
- Grãos Avariados: 8%
- Grãos Esverdeados: 8%
- Quebrados e Amassados: 30%

## Exemplo de Uso
```python
classificacao = ClassificacaoDeSoja()
peso_bruto = 48900  # 48900 kg
tara = 19200  # 19200 kg
umidade = 17  # 17%
impurezas = 1.9  # 1.9%
avariados = 12  # 12%
esverdeados = 13  # 13%
quebrados_amassados = 35  # 35%
```

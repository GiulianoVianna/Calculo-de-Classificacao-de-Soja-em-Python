class ClassificacaoDeSoja:
    def __init__(self):
        # Limites estabelecidos
        self.limite_umidade = 14.0  # 14%
        self.limite_impurezas = 1.0  # 1%
        self.limite_avariados = 8.0  # 8%
        self.limite_esverdeados = 8.0  # 8%
        self.limite_quebrados_amassados = 30.0  # 30%

    def calcular_descontos(self, peso_liquido, umidade, impurezas, avariados, esverdeados, quebrados_amassados):
        descontos = []
        descontos.append(max(0, (umidade - self.limite_umidade) * peso_liquido / 100))
        descontos.append(max(0, (impurezas - self.limite_impurezas) * peso_liquido / 100))
        descontos.append(max(0, (avariados - self.limite_avariados) * peso_liquido / 100))
        descontos.append(max(0, (esverdeados - self.limite_esverdeados) * peso_liquido / 100))
        descontos.append(max(0, (quebrados_amassados - self.limite_quebrados_amassados) * peso_liquido / 100))
        return descontos

    def calcular_peso_liquido(self, peso_bruto, tara):
        return peso_bruto - tara

if __name__ == "__main__":
    classificacao = ClassificacaoDeSoja()

    # Exemplo de dados de entrada
    peso_bruto = 48900  # 48900 kg
    tara = 19200  # 19200 kg
    umidade = 17  # 17%
    impurezas = 1.9  # 1.9%
    avariados = 12  # 12%
    esverdeados = 13  # 13%
    quebrados_amassados = 35  # 35%

    # Calculando o peso líquido
    peso_liquido = classificacao.calcular_peso_liquido(peso_bruto, tara)

    # Calculando os descontos
    descontos = classificacao.calcular_descontos(peso_liquido, umidade, impurezas, avariados, esverdeados, quebrados_amassados)
    desconto_total = sum(descontos)

    # Peso líquido com desconto
    peso_liquido_com_desconto = peso_liquido - desconto_total

    # Imprimindo os resultados
    print(f"Peso Bruto: {peso_bruto}kg")
    print(f"Tara: {tara}kg")
    print(f"Peso Líquido (sem desconto): {peso_liquido}kg")

    nomes_descontos = ["Umidade", "Impurezas", "Avariados", "Esverdeados", "Quebrados e Amassados"]
    for nome, desconto in zip(nomes_descontos, descontos):
        if desconto > 0:
            print(f"{nome} - Desconto: {desconto}kg ({(desconto / peso_liquido * 100):.2f}%)")

    print(f"Desconto Total: {desconto_total}kg ({(desconto_total / peso_liquido * 100):.2f}%)")
    print(f"Peso Líquido (com desconto): {peso_liquido_com_desconto}kg")

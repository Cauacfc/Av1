class Veiculo:
    
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem):
       
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem

    def registrar_manutencao(self, tipo, custo):
        print(f"Manutenção de {tipo} registrada para o veículo {self.marca} {self.modelo} com custo de R${custo:.2f}.")

    def exibir_informacoes(self, detalhado=False):
        if detalhado:
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Ano de Fabricação: {self.ano_fabricacao}")
            print(f"Chassi: {self.chassi}")
            print(f"Cor: {self.cor}")
            print(f"Quilometragem: {self.quilometragem:.2f} km")
        else: 
            print(f"Marca: {self.marca}, Modelo: {self.modelo}, Quilometragem: {self.quilometragem:.2f} km")

class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        
        depreciacao_base = self.quilometragem * 0.1 
        depreciacao_total = depreciacao_base + (taxa_extra * anos_uso)
        print(f"Depreciação calculada para o carro {self.marca} {self.modelo}: R${depreciacao_total:.2f}.")
        return depreciacao_total

    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado)
        if detalhado:
            print(f"Número de Portas: {self.numero_portas}")
            print(f"Tipo de Combustível: {self.tipo_combustivel}")

class CaminhaoCarga(Veiculo):
    
    def __init__(self, marca, modelo, ano_fabricacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        super().__init__(marca, modelo, ano_fabricacao, chassi, cor, quilometragem)
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos

  
    def registrar_vistoria(self, motivo, multa=0):
        print(f"Vistoria registrada para o caminhão {self.marca} {self.modelo}. Motivo: {motivo}.")
        if multa > 0: 
            print(f"Valor da multa: R${multa:.2f}.")
        else: 
            print("Nenhuma multa aplicada.")

   
    def exibir_informacoes(self, detalhado=False):
        super().exibir_informacoes(detalhado) 
        if detalhado: 
            print(f"Capacidade de Carga: {self.capacidade_toneladas:.2f} toneladas")
            print(f"Número de Eixos: {self.eixos}")
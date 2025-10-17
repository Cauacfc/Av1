from veiculos import Veiculo, CarroPasseio, CaminhaoCarga
print("\n---  Principal: Veiculo ---")

veiculo_generico = Veiculo("Ford", "Modelo X", 2020, "CHASSI123", "Prata", 50000.5)
veiculo_generico.exibir_informacoes()
veiculo_generico.exibir_informacoes(detalhado=True)
veiculo_generico.registrar_manutencao("Troca de Óleo", 350.00)
print("\n--- Carro de Passeio 🚗 ---")
carro = CarroPasseio("Volkswagen", "Gol", 2022, "CHASSI456", "Branco", 15000.2, 4, "Gasolina")

carro.exibir_informacoes()
carro.exibir_informacoes(detalhado=True)
carro.registrar_manutencao("Revisão", 800.00)
carro.calcular_depreciacao(anos_uso=2, taxa_extra=50.0)

print("\n--- Caminhão de Carga 🚚---")

caminhao = CaminhaoCarga("Scania", "R450", 2019, "CHASSI789", "Azul", 120000.7, 25.0, 6)


caminhao.exibir_informacoes()
caminhao.exibir_informacoes(detalhado=True)

caminhao.registrar_manutencao("Alinhamento", 600.00)
caminhao.registrar_vistoria("Excesso de peso", 1500.00) 
caminhao.registrar_vistoria("Documentação em ordem") 
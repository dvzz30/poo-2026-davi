class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Quantidade de portas: {self.qtd_portas}")


carro = Carro("Toyota", "Corolla", 4)
carro.exibir_dados()

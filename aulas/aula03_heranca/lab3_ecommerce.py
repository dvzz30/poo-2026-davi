class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem / 100)
        return self.preco


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


livro = Livro("Python para Todos", 80, "Luciano Ramalho")
livro.aplicar_desconto(15)
print(f"Livro: {livro.nome} | Autor: {livro.autor} | Preço com desconto: R$ {livro.preco:.2f}")

eletronico = Eletronico("Smartphone", 1200, "110V")
eletronico.aplicar_desconto(10)
print(f"Eletrônico: {eletronico.nome} | Voltagem: {eletronico.voltagem} | Preço com desconto: R$ {eletronico.preco:.2f}")

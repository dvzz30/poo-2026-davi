class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base  # atributo privado (encapsulado)

    
    def get_salario_base(self):
        return self.__salario_base

  
    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario
        else:
            print(f"[AVISO] Valor inválido ({novo_salario}). "
                  f"O salário base de {self.nome} não foi alterado.")


    def calcular_salario_final(self):
        return self.get_salario_base()

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    
    def calcular_salario_final(self):
        return super().calcular_salario_final() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    ADICIONAL_SENIOR = 1500.00

    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return super().calcular_salario_final() + self.ADICIONAL_SENIOR
        return super().calcular_salario_final()

if __name__ == "__main__":

    
    gerente1 = Gerente("Fernandinho", "M001", 8000.00, 2000.00)
    dev_senior = Desenvolvedor("Marcos Mabola", "M002", 6000.00, "Senior")

    print("=" * 55)
    print("TESTE DE ENCAPSULAMENTO")
    print("=" * 55)


    gerente1.__salario_base = -100

    print(f"Tentativa de alteração direta: gerente1.__salario_base = -100")
    print(f"Valor retornado pelo getter (real): "
          f"R$ {gerente1.get_salario_base():.2f}")
    print("-> O valor protegido não foi alterado, confirmando o encapsulamento.\n")

    
    gerente1.set_salario_base(-500)
    print(f"Após tentativa via setter com valor inválido (-500), "
          f"salário base continua: R$ {gerente1.get_salario_base():.2f}\n")

    print("=" * 55)
    print("SALÁRIOS FINAIS CALCULADOS")
    print("=" * 55)

    funcionarios = [gerente1, dev_senior]

    for func in funcionarios:
        print(f"Nome: {func.nome:<15} | "
              f"Salário Final: R$ {func.calcular_salario_final():.2f}")
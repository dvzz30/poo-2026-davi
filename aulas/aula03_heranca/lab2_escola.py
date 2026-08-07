class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Email: {self.email}")


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, disciplina):
        super().__init__(nome, cpf, email)
        self.disciplina = disciplina

    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Disciplina: {self.disciplina}")


class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, matricula):
        super().__init__(nome, cpf, email)
        self.matricula = matricula

    def exibir_perfil(self):
        super().exibir_perfil()
        print(f"Matrícula: {self.matricula}")


professor = Professor("Ana Silva", "123.456.789-00", "ana@email.com", "Matemática")
aluno = Aluno("Bruno Costa", "987.654.321-00", "bruno@email.com", "2026001")

print("Perfil do professor:")
professor.exibir_perfil()

print("\nPerfil do aluno:")
aluno.exibir_perfil()

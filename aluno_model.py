import uuid
class Aluno:
    def __init__(self,nome, idade,curso,nota):
        self.matricula = uuid.uuid1()
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota

    def __repr__(self):
        return f"matricula : {self.matricula} \n"\
               f"nome: {self.nome}\n"\
               f"idade: {self.idade}\n"\
               f"curso: {self.curso}\n"\
               f"nota: {self.nota}"



if __name__ == "__main__":
    a1 = Aluno("jonas",19,"python", 9.8)
    print(a1)
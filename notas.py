alunos = {}

def adicionar_aluno(nome):
    if nome not in alunos:
        alunos[nome] = []

def adicionar_nota(nome, nota):
    if nome in alunos:
        alunos[nome].append(nota)

def calcular_media(nome):
    if nome in alunos and alunos[nome]:
        return sum(alunos[nome]) / len(alunos[nome])
    return 0

def listar_alunos():
    return alunos
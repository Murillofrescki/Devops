import unittest
from notas import adicionar_aluno, adicionar_nota, calcular_media, listar_alunos, alunos

class TestSistemaNotas(unittest.TestCase):

    def setUp(self):
        # Limpa o dicionário antes de cada teste
        alunos.clear()

    def test_adicionar_aluno(self):
        adicionar_aluno("Murillo")
        self.assertIn("Murillo", alunos)

    def test_adicionar_nota(self):
        adicionar_aluno("Murillo")
        adicionar_nota("Murillo", 8)
        self.assertEqual(alunos["Murillo"], [8])

    def test_calcular_media(self):
        adicionar_aluno("Murillo")
        adicionar_nota("Murillo", 8)
        adicionar_nota("Murillo", 10)
        self.assertEqual(calcular_media("Murillo"), 9)

    def test_media_sem_notas(self):
        adicionar_aluno("Murillo")
        self.assertEqual(calcular_media("Murillo"), 0)

    def test_listar_alunos(self):
        adicionar_aluno("Murillo")
        self.assertIsInstance(listar_alunos(), dict)

    def test_adicionar_nota_sem_aluno(self):
        adicionar_nota("Inexistente", 7)
        self.assertNotIn("Inexistente", alunos)


if __name__ == "__main__":
    unittest.main()
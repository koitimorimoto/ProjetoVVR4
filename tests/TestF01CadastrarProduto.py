import unittest

from src.produto import CatalogoProdutos


class TestF01CadastrarProduto(unittest.TestCase):
    """F01 - Cadastrar produto (Gustavo Nery).
    Cenários de bdd/F01_cadastrar_produto.feature."""

    def setUp(self):
        # Dado que o catálogo de produtos está vazio
        self.catalogo = CatalogoProdutos()

    def test_cadastrar_produto_com_dados_validos(self):
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)

        produto = self.catalogo.obter_por_codigo("P001")
        self.assertIsNotNone(produto)
        self.assertEqual(produto.nome, "Camiseta Azul")
        self.assertAlmostEqual(produto.preco, 49.90, places=2)

    def test_cadastrar_produto_com_codigo_ja_existente(self):
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)

        with self.assertRaises(ValueError) as contexto:
            self.catalogo.cadastrar("P001", "Calça Jeans", 120.00)

        self.assertEqual(str(contexto.exception), "Já existe um produto com o código P001")
        self.assertEqual(self.catalogo.quantidade_de_produtos(), 1)

    def test_cadastrar_produto_sem_nome(self):
        with self.assertRaises(ValueError) as contexto:
            self.catalogo.cadastrar("P002", "", 30.00)

        self.assertEqual(str(contexto.exception), "O nome do produto é obrigatório")
        self.assertEqual(self.catalogo.quantidade_de_produtos(), 0)

    def test_cadastrar_produto_com_preco_zero(self):
        with self.assertRaises(ValueError) as contexto:
            self.catalogo.cadastrar("P003", "Boné", 0.00)

        self.assertEqual(str(contexto.exception), "O preço do produto deve ser maior que zero")
        self.assertEqual(self.catalogo.quantidade_de_produtos(), 0)

    def test_cadastrar_produto_com_preco_negativo(self):
        with self.assertRaises(ValueError) as contexto:
            self.catalogo.cadastrar("P004", "Meia", -10.00)

        self.assertEqual(str(contexto.exception), "O preço do produto deve ser maior que zero")
        self.assertEqual(self.catalogo.quantidade_de_produtos(), 0)


if __name__ == "__main__":
    unittest.main()

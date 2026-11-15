import unittest

from src.produto import CatalogoProdutos
from src.estoque import Estoque


class TestF04AdicionarProdutoAoEstoque(unittest.TestCase):
    """F04 - Adicionar produto ao estoque (Felipe Braga).
    Cenários de bdd/F04_adicionar_produto_ao_estoque.feature."""

    def setUp(self):
        # Contexto: Dado que existe o produto "P001", "Camiseta Azul", 49.90
        self.catalogo = CatalogoProdutos()
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)
        self.estoque = Estoque(self.catalogo)

    def test_adicionar_quantidade_valida_ao_estoque(self):
        self.estoque.adicionar("P001", 10)

        self.assertEqual(self.estoque.quantidade("P001"), 10)

    def test_adicionar_quantidade_a_um_produto_que_ja_possui_estoque(self):
        self.estoque.adicionar("P001", 10)

        self.estoque.adicionar("P001", 5)

        self.assertEqual(self.estoque.quantidade("P001"), 15)

    def test_adicionar_quantidade_zero_ao_estoque(self):
        with self.assertRaises(ValueError) as contexto:
            self.estoque.adicionar("P001", 0)

        self.assertEqual(str(contexto.exception), "A quantidade deve ser maior que zero")
        self.assertEqual(self.estoque.quantidade("P001"), 0)

    def test_adicionar_quantidade_negativa_ao_estoque(self):
        with self.assertRaises(ValueError) as contexto:
            self.estoque.adicionar("P001", -3)

        self.assertEqual(str(contexto.exception), "A quantidade deve ser maior que zero")
        self.assertEqual(self.estoque.quantidade("P001"), 0)

    def test_adicionar_ao_estoque_um_produto_nao_cadastrado(self):
        with self.assertRaises(ValueError) as contexto:
            self.estoque.adicionar("P999", 10)

        self.assertEqual(str(contexto.exception), "Produto não encontrado: P999")


if __name__ == "__main__":
    unittest.main()

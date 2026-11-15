import unittest

from src.produto import CatalogoProdutos
from src.estoque import Estoque
from src.carrinho import Carrinho


class TestF06RemoverItemDoCarrinho(unittest.TestCase):
    """F06 - Remover item do carrinho (Integrante 3).
    Cenários de bdd/F06_remover_item_do_carrinho.feature."""

    def setUp(self):
        # Contexto: P001 e P002 cadastrados, 10 unidades de cada em estoque,
        # carrinho com 2 unidades de P001 e 1 unidade de P002
        self.catalogo = CatalogoProdutos()
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)
        self.catalogo.cadastrar("P002", "Calça Jeans", 120.00)
        self.estoque = Estoque(self.catalogo)
        self.estoque.adicionar("P001", 10)
        self.estoque.adicionar("P002", 10)
        self.carrinho = Carrinho(self.catalogo, self.estoque)
        self.carrinho.adicionar_item("P001", 2)
        self.carrinho.adicionar_item("P002", 1)

    def test_remover_item_que_esta_no_carrinho(self):
        self.carrinho.remover_item("P001")

        self.assertEqual(self.carrinho.quantidade_do_item("P001"), 0)
        self.assertEqual(self.carrinho.quantidade_de_itens(), 1)
        self.assertEqual(self.carrinho.quantidade_do_item("P002"), 1)

    def test_remover_item_que_nao_esta_no_carrinho(self):
        with self.assertRaises(ValueError) as contexto:
            self.carrinho.remover_item("P003")

        self.assertEqual(str(contexto.exception), "Item não está no carrinho: P003")
        self.assertEqual(self.carrinho.quantidade_de_itens(), 2)


if __name__ == "__main__":
    unittest.main()
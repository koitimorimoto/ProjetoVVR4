import unittest

from src.produto import CatalogoProdutos
from src.estoque import Estoque
from src.carrinho import Carrinho


class TestF05AdicionarItemAoCarrinho(unittest.TestCase):
    """F05 - Adicionar item ao carrinho (Integrante 3).
    Cenários de bdd/F05_adicionar_item_ao_carrinho.feature."""

    def setUp(self):
        # Contexto: produto P001 cadastrado, com 5 unidades em estoque,
        # e o carrinho vazio
        self.catalogo = CatalogoProdutos()
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)
        self.estoque = Estoque(self.catalogo)
        self.estoque.adicionar("P001", 5)
        self.carrinho = Carrinho(self.catalogo, self.estoque)

    def test_adicionar_item_com_quantidade_disponivel_em_estoque(self):
        self.carrinho.adicionar_item("P001", 2)

        self.assertEqual(self.carrinho.quantidade_do_item("P001"), 2)

    def test_adicionar_novamente_um_item_que_ja_esta_no_carrinho(self):
        self.carrinho.adicionar_item("P001", 2)

        self.carrinho.adicionar_item("P001", 3)

        self.assertEqual(self.carrinho.quantidade_do_item("P001"), 5)
        self.assertEqual(self.carrinho.quantidade_de_itens(), 1)

    def test_adicionar_item_com_quantidade_zero(self):
        with self.assertRaises(ValueError) as contexto:
            self.carrinho.adicionar_item("P001", 0)

        self.assertEqual(str(contexto.exception), "A quantidade deve ser maior que zero")
        self.assertEqual(self.carrinho.quantidade_de_itens(), 0)

    def test_adicionar_item_com_quantidade_maior_que_o_estoque(self):
        with self.assertRaises(ValueError) as contexto:
            self.carrinho.adicionar_item("P001", 6)

        self.assertEqual(
            str(contexto.exception),
            "Quantidade indisponível em estoque para o produto P001",
        )
        self.assertEqual(self.carrinho.quantidade_de_itens(), 0)

    def test_adicionar_item_repetido_ultrapassando_o_estoque(self):
        self.carrinho.adicionar_item("P001", 4)

        with self.assertRaises(ValueError) as contexto:
            self.carrinho.adicionar_item("P001", 2)

        self.assertEqual(
            str(contexto.exception),
            "Quantidade indisponível em estoque para o produto P001",
        )
        self.assertEqual(self.carrinho.quantidade_do_item("P001"), 4)

    def test_adicionar_ao_carrinho_um_produto_nao_cadastrado(self):
        with self.assertRaises(ValueError) as contexto:
            self.carrinho.adicionar_item("P999", 1)

        self.assertEqual(str(contexto.exception), "Produto não encontrado: P999")
        self.assertEqual(self.carrinho.quantidade_de_itens(), 0)


if __name__ == "__main__":
    unittest.main()
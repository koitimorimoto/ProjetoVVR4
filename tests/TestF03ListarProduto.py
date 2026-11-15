import unittest

from src.produto import CatalogoProdutos


class TestF03ListarProduto(unittest.TestCase):
    """F03 - Listar produto (Felipe Braga).
    Cenários de bdd/F03_listar_produto.feature."""

    def setUp(self):
        self.catalogo = CatalogoProdutos()

    def test_listar_todos_os_produtos_cadastrados(self):
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)
        self.catalogo.cadastrar("P002", "Calça Jeans", 120.00)
        self.catalogo.cadastrar("P003", "Camiseta Branca", 39.90)

        produtos = self.catalogo.listar()

        self.assertEqual(len(produtos), 3)
        codigos = [produto.codigo for produto in produtos]
        self.assertEqual(codigos, ["P001", "P002", "P003"])

    def test_listar_produtos_com_o_catalogo_vazio(self):
        produtos = self.catalogo.listar()

        self.assertEqual(produtos, [])


if __name__ == "__main__":
    unittest.main()

import unittest

from src.produto import CatalogoProdutos


class TestF02BuscarProduto(unittest.TestCase):
    """F02 - Buscar produto (Gustavo Nery).
    Cenários de bdd/F02_buscar_produto.feature."""

    def setUp(self):
        # Contexto: Dado que existem os produtos cadastrados
        self.catalogo = CatalogoProdutos()
        self.catalogo.cadastrar("P001", "Camiseta Azul", 49.90)
        self.catalogo.cadastrar("P002", "Calça Jeans", 120.00)
        self.catalogo.cadastrar("P003", "Camiseta Branca", 39.90)

    def test_buscar_produto_pelo_nome_sem_diferenciar_maiusculas_e_minusculas(self):
        resultado = self.catalogo.buscar_por_nome("CAMISETA")

        self.assertEqual(len(resultado), 2)
        codigos = [produto.codigo for produto in resultado]
        self.assertCountEqual(codigos, ["P001", "P003"])

    def test_buscar_produto_por_parte_do_nome(self):
        resultado = self.catalogo.buscar_por_nome("jeans")

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].codigo, "P002")

    def test_buscar_produto_que_nao_existe(self):
        resultado = self.catalogo.buscar_por_nome("Tênis")

        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()

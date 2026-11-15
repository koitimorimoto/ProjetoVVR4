"""Módulo de produtos: cadastro e consulta do catálogo do e-commerce."""


class Produto:
    """Produto vendido na loja, identificado por um código único."""

    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class CatalogoProdutos:
    """Catálogo que armazena os produtos cadastrados, indexados pelo código."""

    def __init__(self):
        self._produtos = {}

    def listar(self):
        """Retorna todos os produtos na ordem de cadastro.

        Devolve uma nova lista (cópia), para que alterações feitas nela
        não afetem o catálogo. Sem produtos, retorna lista vazia.
        """
        return list(self._produtos.values())

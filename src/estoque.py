"""Módulo de estoque: controle da quantidade disponível de cada produto."""

MENSAGEM_PRODUTO_NAO_ENCONTRADO = "Produto não encontrado: {codigo}"
MENSAGEM_QUANTIDADE_INVALIDA = "A quantidade deve ser maior que zero"


class Estoque:
    """Guarda a quantidade em estoque de cada produto cadastrado no catálogo."""

    def __init__(self, catalogo):
        self._catalogo = catalogo
        self._quantidades = {}

    def adicionar(self, codigo, quantidade):
        """Adiciona unidades de um produto ao estoque, somando à quantidade atual.

        Lança ValueError se o produto não estiver cadastrado ou se a
        quantidade não for maior que zero.
        """
        self._validar_produto_cadastrado(codigo)
        if quantidade <= 0:
            raise ValueError(MENSAGEM_QUANTIDADE_INVALIDA)
        self._quantidades[codigo] = self.quantidade(codigo) + quantidade

    def quantidade(self, codigo):
        """Retorna as unidades em estoque do produto (0 se não houver)."""
        return self._quantidades.get(codigo, 0)

    def _validar_produto_cadastrado(self, codigo):
        if self._catalogo.obter_por_codigo(codigo) is None:
            raise ValueError(MENSAGEM_PRODUTO_NAO_ENCONTRADO.format(codigo=codigo))

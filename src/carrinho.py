"""Módulo do carrinho de compras do e-commerce."""

from src.estoque import MENSAGEM_QUANTIDADE_INVALIDA

MENSAGEM_ESTOQUE_INSUFICIENTE = "Quantidade indisponível em estoque para o produto {codigo}"
MENSAGEM_ITEM_FORA_DO_CARRINHO = "Item não está no carrinho: {codigo}"


class Carrinho:
    """Carrinho de compras: guarda a quantidade de cada produto escolhido."""

    def __init__(self, catalogo, estoque):
        self._catalogo = catalogo
        self._estoque = estoque
        self._itens = {}

    def adicionar_item(self, codigo, quantidade):
        """Adiciona unidades de um produto ao carrinho.

        Se o produto já estiver no carrinho, soma as quantidades. Lança
        ValueError se a quantidade não for maior que zero, se o produto não
        existir ou se o total no carrinho ultrapassar o estoque disponível.
        """
        if quantidade <= 0:
            raise ValueError(MENSAGEM_QUANTIDADE_INVALIDA)
        nova_quantidade = self.quantidade_do_item(codigo) + quantidade
        self._validar_disponibilidade(codigo, nova_quantidade)
        self._itens[codigo] = nova_quantidade

    def remover_item(self, codigo):
        """Remove o produto do carrinho, com todas as suas unidades.

        Lança ValueError se o produto não estiver no carrinho.
        """
        self._validar_item_no_carrinho(codigo)
        del self._itens[codigo]

    def quantidade_do_item(self, codigo):
        """Retorna as unidades do produto no carrinho (0 se não estiver)."""
        return self._itens.get(codigo, 0)

    def quantidade_de_itens(self):
        """Retorna quantos produtos diferentes estão no carrinho."""
        return len(self._itens)

    def calcular_total(self):
        """Retorna a soma de preço x quantidade de todos os itens.

        Carrinho vazio retorna 0.
        """
        return sum(
            self._subtotal(codigo, quantidade)
            for codigo, quantidade in self._itens.items()
        )

    def _subtotal(self, codigo, quantidade):
        preco = self._catalogo.obter_por_codigo(codigo).preco
        return preco * quantidade

    def _validar_disponibilidade(self, codigo, quantidade_desejada):
        disponivel = self._estoque.consultar_disponibilidade(codigo)
        if quantidade_desejada > disponivel:
            raise ValueError(MENSAGEM_ESTOQUE_INSUFICIENTE.format(codigo=codigo))

    def _validar_item_no_carrinho(self, codigo):
        if codigo not in self._itens:
            raise ValueError(MENSAGEM_ITEM_FORA_DO_CARRINHO.format(codigo=codigo))
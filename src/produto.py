"""Módulo de produtos: cadastro e consulta do catálogo do e-commerce."""

MENSAGEM_CODIGO_DUPLICADO = "Já existe um produto com o código {codigo}"
MENSAGEM_NOME_OBRIGATORIO = "O nome do produto é obrigatório"
MENSAGEM_PRECO_INVALIDO = "O preço do produto deve ser maior que zero"


def _normalizar(texto):
    """Padroniza um texto para comparação sem diferenciar maiúsculas/minúsculas."""
    return texto.lower()


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

    def cadastrar(self, codigo, nome, preco):
        """Cadastra um novo produto após validar as regras de negócio.

        Lança ValueError se o código já existir, se o nome estiver vazio
        ou se o preço não for maior que zero.
        """
        self._validar_novo_produto(codigo, nome, preco)
        self._produtos[codigo] = Produto(codigo, nome, preco)

    def obter_por_codigo(self, codigo):
        """Retorna o produto com o código informado ou None se não existir."""
        return self._produtos.get(codigo)

    def quantidade_de_produtos(self):
        """Retorna quantos produtos estão cadastrados no catálogo."""
        return len(self._produtos)

    def buscar_por_nome(self, termo):
        """Retorna os produtos cujo nome contém o termo, sem diferenciar
        maiúsculas de minúsculas. Sem resultados, retorna lista vazia."""
        termo_normalizado = _normalizar(termo)
        return [
            produto
            for produto in self._produtos.values()
            if termo_normalizado in _normalizar(produto.nome)
        ]

    def listar(self):
        """Retorna todos os produtos na ordem de cadastro.

        Devolve uma nova lista (cópia), para que alterações feitas nela
        não afetem o catálogo. Sem produtos, retorna lista vazia.
        """
        return list(self._produtos.values())

    def _validar_novo_produto(self, codigo, nome, preco):
        if codigo in self._produtos:
            raise ValueError(MENSAGEM_CODIGO_DUPLICADO.format(codigo=codigo))
        if not nome:
            raise ValueError(MENSAGEM_NOME_OBRIGATORIO)
        if preco <= 0:
            raise ValueError(MENSAGEM_PRECO_INVALIDO)

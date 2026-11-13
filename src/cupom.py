class GerenciadorCupons:
    def __init__(self):
        self.cupons = {}

    def cadastrar(self, codigo, percentual, validade, valor_minimo):
        self.cupons[codigo] = {
            "percentual": percentual,
            "validade": validade,
            "valor_minimo": valor_minimo,
        }

    def aplicar(self, codigo, valor_pedido, data_atual):
        if codigo not in self.cupons:
            raise ValueError(f"Cupom não encontrado: {codigo}")

        cupom = self.cupons[codigo]

        if data_atual > cupom["validade"]:
            raise ValueError(f"Cupom expirado: {codigo}")

        if valor_pedido < cupom["valor_minimo"]:
            raise ValueError(
                f"Valor mínimo do pedido para o cupom {codigo} "
                f"é R$ {cupom['valor_minimo']:.2f}"
            )

        desconto = valor_pedido * cupom["percentual"] / 100
        return valor_pedido - desconto

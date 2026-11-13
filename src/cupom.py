from dataclasses import dataclass
from datetime import date

_CEM_POR_CENTO = 100


@dataclass
class Cupom:
    codigo: str
    percentual: float
    validade: date
    valor_minimo: float

    def calcular_desconto(self, valor_pedido: float) -> float:
        return valor_pedido * self.percentual / _CEM_POR_CENTO


class GerenciadorCupons:
    def __init__(self):
        self._cupons: dict[str, Cupom] = {}

    def cadastrar(
        self,
        codigo: str,
        percentual: float,
        validade: date,
        valor_minimo: float,
    ) -> None:
        self._cupons[codigo] = Cupom(codigo, percentual, validade, valor_minimo)

    def aplicar(self, codigo: str, valor_pedido: float, data_atual: date) -> float:
        cupom = self._obter_cupom(codigo)
        self._validar_cupom(cupom, valor_pedido, data_atual)
        return valor_pedido - cupom.calcular_desconto(valor_pedido)

    def _obter_cupom(self, codigo: str) -> Cupom:
        if codigo not in self._cupons:
            raise ValueError(f"Cupom não encontrado: {codigo}")
        return self._cupons[codigo]

    @staticmethod
    def _validar_cupom(
        cupom: Cupom, valor_pedido: float, data_atual: date
    ) -> None:
        if data_atual > cupom.validade:
            raise ValueError(f"Cupom expirado: {cupom.codigo}")

        if valor_pedido < cupom.valor_minimo:
            raise ValueError(
                f"Valor mínimo do pedido para o cupom {cupom.codigo} "
                f"é R$ {cupom.valor_minimo:.2f}"
            )

import unittest
from datetime import date
from src.cupom import GerenciadorCupons

class TestF09AplicarCupomDeDesconto(unittest.TestCase):

    def setUp(self):
        self.cupons = GerenciadorCupons()
        self.cupons.cadastrar("DESC10", 10, date(2026, 12, 31), 100.00)
        self.cupons.cadastrar("VELHO20", 20, date(2025, 12, 31), 50.00)
        self.data_atual = date(2026, 11, 12)

    def test_aplicar_cupom_valido_em_pedido_acima_do_valor_minimo(self):
        valor_final = self.cupons.aplicar("DESC10", 200.00, self.data_atual)

        self.assertAlmostEqual(valor_final, 180.00, places=2)

    def test_aplicar_cupom_valido_em_pedido_igual_ao_valor_minimo(self):
        valor_final = self.cupons.aplicar("DESC10", 100.00, self.data_atual)

        self.assertAlmostEqual(valor_final, 90.00, places=2)

    def test_aplicar_cupom_inexistente(self):
        with self.assertRaises(ValueError) as contexto:
            self.cupons.aplicar("NAOEXISTE", 200.00, self.data_atual)

        self.assertEqual(str(contexto.exception), "Cupom não encontrado: NAOEXISTE")

    def test_aplicar_cupom_expirado(self):
        with self.assertRaises(ValueError) as contexto:
            self.cupons.aplicar("VELHO20", 200.00, self.data_atual)

        self.assertEqual(str(contexto.exception), "Cupom expirado: VELHO20")

    def test_aplicar_cupom_em_pedido_abaixo_do_valor_minimo(self):
        with self.assertRaises(ValueError) as contexto:
            self.cupons.aplicar("DESC10", 99.99, self.data_atual)

        self.assertEqual(
            str(contexto.exception),
            "Valor mínimo do pedido para o cupom DESC10 é R$ 100.00",
        )

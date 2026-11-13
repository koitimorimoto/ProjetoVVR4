import unittest
from src.frete import calcular_frete

class TestF10CalcularFrete(unittest.TestCase):

    def test_frete_gratis_para_pedido_acima_de_200(self):
        frete = calcular_frete(250.00, "80215901")

        self.assertAlmostEqual(frete, 0.00, places=2)

    def test_frete_fixo_para_pedido_abaixo_de_200(self):
        frete = calcular_frete(150.00, "80215901")

        self.assertAlmostEqual(frete, 20.00, places=2)

    def test_frete_fixo_para_pedido_de_exatamente_200(self):
        frete = calcular_frete(200.00, "80215901")

        self.assertAlmostEqual(frete, 20.00, places=2)

    def test_calcular_frete_com_cep_com_menos_de_8_digitos(self):
        with self.assertRaises(ValueError) as contexto:
            calcular_frete(150.00, "8021590")

        self.assertEqual(
            str(contexto.exception),
            "CEP inválido: deve conter exatamente 8 dígitos numéricos",
        )

    def test_calcular_frete_com_cep_contendo_caracteres_nao_numericos(self):
        with self.assertRaises(ValueError) as contexto:
            calcular_frete(150.00, "8021A901")

        self.assertEqual(
            str(contexto.exception),
            "CEP inválido: deve conter exatamente 8 dígitos numéricos",
        )


if __name__ == "__main__":
    unittest.main()

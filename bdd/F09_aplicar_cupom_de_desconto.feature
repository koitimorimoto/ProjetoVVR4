Funcionalidade: F09 - Aplicar cupom de desconto
  Como cliente da loja
  Quero aplicar um cupom de desconto ao meu pedido
  Para pagar um valor menor

  Contexto:
    Dado que existem os cupons cadastrados:
      | codigo  | desconto | validade   | valor_minimo |
      | DESC10  | 10%      | 31/12/2026 | 100.00       |
      | VELHO20 | 20%      | 31/12/2025 | 50.00        |
    E a data atual é 12/11/2026

#Casos de sucesso
  Cenário: Aplicar cupom válido em pedido acima do valor mínimo
    Quando eu aplico o cupom "DESC10" em um pedido de 200.00
    Então o valor do pedido com desconto deve ser 180.00

  Cenário: Aplicar cupom válido em pedido igual ao valor mínimo
    Quando eu aplico o cupom "DESC10" em um pedido de 100.00
    Então o valor do pedido com desconto deve ser 90.00

#Casos de exceção
  Cenário: Aplicar cupom inexistente
    Quando eu aplico o cupom "NAOEXISTE" em um pedido de 200.00
    Então deve ser exibido o erro "Cupom não encontrado: NAOEXISTE"

  Cenário: Aplicar cupom expirado
    Quando eu aplico o cupom "VELHO20" em um pedido de 200.00
    Então deve ser exibido o erro "Cupom expirado: VELHO20"

  Cenário: Aplicar cupom em pedido abaixo do valor mínimo
    Quando eu aplico o cupom "DESC10" em um pedido de 99.99
    Então deve ser exibido o erro "Valor mínimo do pedido para o cupom DESC10 é R$ 100.00"

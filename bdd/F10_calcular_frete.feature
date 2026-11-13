Funcionalidade: F10 - Calcular frete
  Como cliente da loja
  Quero saber o valor do frete do meu pedido
  Para conhecer o custo total da compra

#Casos de sucesso
  Cenário: Frete grátis para pedido acima de R$ 200
    Quando eu calculo o frete de um pedido de 250.00 para o CEP "80215901"
    Então o valor do frete deve ser 0.00

  Cenário: Frete fixo para pedido abaixo de R$ 200
    Quando eu calculo o frete de um pedido de 150.00 para o CEP "80215901"
    Então o valor do frete deve ser 20.00

  Cenário: Frete fixo para pedido de exatamente R$ 200
    Quando eu calculo o frete de um pedido de 200.00 para o CEP "80215901"
    Então o valor do frete deve ser 20.00

#Casos de exceção
  Cenário: Calcular frete com CEP com menos de 8 dígitos
    Quando eu calculo o frete de um pedido de 150.00 para o CEP "8021590"
    Então deve ser exibido o erro "CEP inválido: deve conter exatamente 8 dígitos numéricos"

  Cenário: Calcular frete com CEP contendo caracteres não numéricos
    Quando eu calculo o frete de um pedido de 150.00 para o CEP "8021A901"
    Então deve ser exibido o erro "CEP inválido: deve conter exatamente 8 dígitos numéricos"

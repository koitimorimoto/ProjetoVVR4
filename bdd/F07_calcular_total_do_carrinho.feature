Funcionalidade: F07 - Calcular total do carrinho
  Como cliente da loja
  Quero ver o valor total do meu carrinho
  Para saber quanto vou pagar pelos produtos

  Contexto:
    Dado que existem os produtos cadastrados:
      | codigo | nome          | preco  |
      | P001   | Camiseta Azul | 49.90  |
      | P002   | Calça Jeans   | 120.00 |
    E o produto "P001" possui 10 unidades em estoque
    E o produto "P002" possui 10 unidades em estoque

#Casos de sucesso
  Cenário: Calcular total de carrinho com vários itens
    Dado que o carrinho contém 2 unidades do produto "P001"
    E o carrinho contém 1 unidade do produto "P002"
    Quando eu calculo o total do carrinho
    Então o total deve ser 219.80

  Cenário: Recalcular total após remover um item
    Dado que o carrinho contém 2 unidades do produto "P001"
    E o carrinho contém 1 unidade do produto "P002"
    E eu removo o produto "P002" do carrinho
    Quando eu calculo o total do carrinho
    Então o total deve ser 99.80

#Casos de exceção
  Cenário: Calcular total de carrinho vazio
    Dado que o meu carrinho está vazio
    Quando eu calculo o total do carrinho
    Então o total deve ser 0.00

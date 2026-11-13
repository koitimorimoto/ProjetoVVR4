Funcionalidade: F06 - Remover item do carrinho
  Como cliente da loja
  Quero remover itens do meu carrinho
  Para comprar apenas o que realmente desejo

  Contexto:
    Dado que existem os produtos cadastrados:
      | codigo | nome          | preco  |
      | P001   | Camiseta Azul | 49.90  |
      | P002   | Calça Jeans   | 120.00 |
    E o produto "P001" possui 10 unidades em estoque
    E o produto "P002" possui 10 unidades em estoque
    E o carrinho contém 2 unidades do produto "P001"
    E o carrinho contém 1 unidade do produto "P002"

#Caso de sucesso
  Cenário: Remover item que está no carrinho
    Quando eu removo o produto "P001" do carrinho
    Então o carrinho não deve conter o produto "P001"
    E o carrinho deve conter 1 unidade do produto "P002"

#Caso de exceção
  Cenário: Remover item que não está no carrinho
    Quando eu removo o produto "P003" do carrinho
    Então deve ser exibido o erro "Item não está no carrinho: P003"
    E o carrinho deve continuar com 2 itens

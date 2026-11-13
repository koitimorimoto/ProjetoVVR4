Funcionalidade: F05 - Adicionar item ao carrinho
  Como cliente da loja
  Quero adicionar produtos ao meu carrinho
  Para comprá-los ao finalizar o pedido

  Contexto:
    Dado que existe o produto com código "P001", nome "Camiseta Azul" e preço 49.90
    E o produto "P001" possui 5 unidades em estoque
    E o meu carrinho está vazio

#Casos de sucesso
  Cenário: Adicionar item com quantidade disponível em estoque
    Quando eu adiciono 2 unidades do produto "P001" ao carrinho
    Então o carrinho deve conter 2 unidades do produto "P001"

  Cenário: Adicionar novamente um item que já está no carrinho
    Dado que o carrinho contém 2 unidades do produto "P001"
    Quando eu adiciono 3 unidades do produto "P001" ao carrinho
    Então o carrinho deve conter 5 unidades do produto "P001"
    E o carrinho deve ter 1 item

#Casos de exceção
  Cenário: Adicionar item com quantidade zero
    Quando eu adiciono 0 unidades do produto "P001" ao carrinho
    Então deve ser exibido o erro "A quantidade deve ser maior que zero"
    E o carrinho deve continuar vazio

  Cenário: Adicionar item com quantidade maior que o estoque
    Quando eu adiciono 6 unidades do produto "P001" ao carrinho
    Então deve ser exibido o erro "Quantidade indisponível em estoque para o produto P001"
    E o carrinho deve continuar vazio

  Cenário: Adicionar item repetido ultrapassando o estoque
    Dado que o carrinho contém 4 unidades do produto "P001"
    Quando eu adiciono 2 unidades do produto "P001" ao carrinho
    Então deve ser exibido o erro "Quantidade indisponível em estoque para o produto P001"
    E o carrinho deve continuar com 4 unidades do produto "P001"

  Cenário: Adicionar ao carrinho um produto não cadastrado
    Quando eu adiciono 1 unidade do produto "P999" ao carrinho
    Então deve ser exibido o erro "Produto não encontrado: P999"
    E o carrinho deve continuar vazio

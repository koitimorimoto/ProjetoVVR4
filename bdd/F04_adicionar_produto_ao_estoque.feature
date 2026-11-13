Funcionalidade: F04 - Adicionar produto ao estoque
  Como administrador da loja
  Quero adicionar unidades de um produto ao estoque
  Para que os clientes possam comprá-lo

  Contexto:
    Dado que existe o produto com código "P001", nome "Camiseta Azul" e preço 49.90

#Casos de sucesso
  Cenário: Adicionar quantidade válida ao estoque
    Dado que o produto "P001" não possui unidades em estoque
    Quando eu adiciono 10 unidades do produto "P001" ao estoque
    Então o estoque do produto "P001" deve ser 10

  Cenário: Adicionar quantidade a um produto que já possui estoque
    Dado que o produto "P001" possui 10 unidades em estoque
    Quando eu adiciono 5 unidades do produto "P001" ao estoque
    Então o estoque do produto "P001" deve ser 15

#Casos de exceção
  Cenário: Adicionar quantidade zero ao estoque
    Quando eu adiciono 0 unidades do produto "P001" ao estoque
    Então deve ser exibido o erro "A quantidade deve ser maior que zero"
    E o estoque do produto "P001" deve ser 0

  Cenário: Adicionar quantidade negativa ao estoque
    Quando eu adiciono -3 unidades do produto "P001" ao estoque
    Então deve ser exibido o erro "A quantidade deve ser maior que zero"
    E o estoque do produto "P001" deve ser 0

  Cenário: Adicionar ao estoque um produto não cadastrado
    Quando eu adiciono 10 unidades do produto "P999" ao estoque
    Então deve ser exibido o erro "Produto não encontrado: P999"

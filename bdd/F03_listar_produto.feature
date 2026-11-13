Funcionalidade: F03 - Listar produto
  Como cliente da loja
  Quero ver a lista de todos os produtos
  Para conhecer o que está disponível no catálogo

#Caso de sucesso
  Cenário: Listar todos os produtos cadastrados
    Dado que existem os produtos cadastrados:
      | codigo | nome            | preco  |
      | P001   | Camiseta Azul   | 49.90  |
      | P002   | Calça Jeans     | 120.00 |
      | P003   | Camiseta Branca | 39.90  |
    Quando eu listo os produtos
    Então devem ser retornados 3 produtos
    E os produtos devem estar na ordem "P001", "P002" e "P003"

#Caso de exceção
  Cenário: Listar produtos com o catálogo vazio
    Dado que o catálogo de produtos está vazio
    Quando eu listo os produtos
    Então deve ser retornada uma lista vazia

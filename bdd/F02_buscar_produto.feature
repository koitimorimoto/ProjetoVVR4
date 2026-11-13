Funcionalidade: F02 - Buscar produto
  Como cliente da loja
  Quero buscar produtos pelo nome
  Para encontrar rapidamente o que desejo comprar

  Contexto:
    Dado que existem os produtos cadastrados:
      | codigo | nome            | preco  |
      | P001   | Camiseta Azul   | 49.90  |
      | P002   | Calça Jeans     | 120.00 |
      | P003   | Camiseta Branca | 39.90  |

#Casos de sucesso
  Cenário: Buscar produto pelo nome sem diferenciar maiúsculas e minúsculas
    Quando eu busco produtos pelo nome "CAMISETA"
    Então devem ser retornados 2 produtos
    E o resultado deve conter os produtos "P001" e "P003"

  Cenário: Buscar produto por parte do nome
    Quando eu busco produtos pelo nome "jeans"
    Então deve ser retornado 1 produto
    E o resultado deve conter o produto "P002"

#Caso de exceção
  Cenário: Buscar produto que não existe
    Quando eu busco produtos pelo nome "Tênis"
    Então deve ser retornada uma lista vazia

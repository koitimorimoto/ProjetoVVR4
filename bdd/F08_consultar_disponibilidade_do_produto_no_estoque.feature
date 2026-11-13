Funcionalidade: F08 - Consultar disponibilidade do produto no estoque
  Como cliente da loja
  Quero consultar quantas unidades de um produto estão disponíveis
  Para saber se posso comprá-lo

  Contexto:
    Dado que existem os produtos cadastrados:
      | codigo | nome          | preco  |
      | P001   | Camiseta Azul | 49.90  |
      | P002   | Calça Jeans   | 120.00 |

#Casos de sucesso
  Cenário: Consultar disponibilidade de produto com estoque
    Dado que o produto "P001" possui 15 unidades em estoque
    Quando eu consulto a disponibilidade do produto "P001"
    Então a quantidade disponível deve ser 15

  Cenário: Consultar disponibilidade de produto cadastrado sem estoque
    Quando eu consulto a disponibilidade do produto "P002"
    Então a quantidade disponível deve ser 0

#Caso de exceção
  Cenário: Consultar disponibilidade de produto inexistente
    Quando eu consulto a disponibilidade do produto "P999"
    Então deve ser exibido o erro "Produto não encontrado: P999"

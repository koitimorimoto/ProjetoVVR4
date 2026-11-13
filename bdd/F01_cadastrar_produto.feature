Funcionalidade: F01 - Cadastrar produto
  Como administrador da loja
  Quero cadastrar produtos no catálogo
  Para que eles possam ser vendidos no e-commerce

#Caso de sucesso
  Cenário: Cadastrar produto com dados válidos
    Dado que o catálogo de produtos está vazio
    Quando eu cadastro o produto com código "P001", nome "Camiseta Azul" e preço 49.90
    Então o produto "P001" deve estar cadastrado no catálogo
    E o produto "P001" deve ter nome "Camiseta Azul" e preço 49.90

#Casos de exceção
  Cenário: Cadastrar produto com código já existente
    Dado que existe o produto com código "P001", nome "Camiseta Azul" e preço 49.90
    Quando eu cadastro o produto com código "P001", nome "Calça Jeans" e preço 120.00
    Então deve ser exibido o erro "Já existe um produto com o código P001"
    E o catálogo deve continuar com 1 produto

  Cenário: Cadastrar produto sem nome
    Dado que o catálogo de produtos está vazio
    Quando eu cadastro o produto com código "P002", nome "" e preço 30.00
    Então deve ser exibido o erro "O nome do produto é obrigatório"
    E o catálogo deve continuar vazio

  Cenário: Cadastrar produto com preço zero
    Dado que o catálogo de produtos está vazio
    Quando eu cadastro o produto com código "P003", nome "Boné" e preço 0.00
    Então deve ser exibido o erro "O preço do produto deve ser maior que zero"
    E o catálogo deve continuar vazio

  Cenário: Cadastrar produto com preço negativo
    Dado que o catálogo de produtos está vazio
    Quando eu cadastro o produto com código "P004", nome "Meia" e preço -10.00
    Então deve ser exibido o erro "O preço do produto deve ser maior que zero"
    E o catálogo deve continuar vazio

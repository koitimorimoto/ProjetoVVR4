def calcular_frete(valor_pedido, cep):
    if len(cep) != 8 or not cep.isdigit():
        raise ValueError(
            "CEP inválido: deve conter exatamente 8 dígitos numéricos"
        )

    if valor_pedido > 200:
        return 0.00

    return 20.00

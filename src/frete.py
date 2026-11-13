TAMANHO_CEP = 8
LIMITE_FRETE_GRATIS = 200.00
VALOR_FRETE_GRATIS = 0.00
VALOR_FRETE_FIXO = 20.00
MENSAGEM_CEP_INVALIDO = (
    "CEP inválido: deve conter exatamente 8 dígitos numéricos"
)


def calcular_frete(valor_pedido, cep):
    if not _cep_valido(cep):
        raise ValueError(MENSAGEM_CEP_INVALIDO)

    if valor_pedido > LIMITE_FRETE_GRATIS:
        return VALOR_FRETE_GRATIS

    return VALOR_FRETE_FIXO


def _cep_valido(cep):
    return len(cep) == TAMANHO_CEP and cep.isdigit()

def aumentar_salario(salario, porcentagem):
    novo_salario = salario + (salario * (porcentagem/100))
    return novo_salario

def desconto_salario(salario, porcentagem):
    salario_com_desconto = salario - (salario * (porcentagem/100))
    return salario_com_desconto

def variacao_percentual(salario_velho, salario_novo):
    variacao = ((salario_novo - salario_velho) / salario_velho) * 100
    return variacao

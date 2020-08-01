saldo = 1000
salario = 4000
despesas = 2967
# saber se a pessoa bateu a meta, se o saldo estiver positivo, oq sobrou no mês foi mais de 20%

'''meta = saldo > 0 and salario - despesas >= 0.2 * salario

# saldo recebe maior que 0, ou saldo positivo, e quer saber se salario menos depesas é maior ou iqual a 20% do salario, forma em python

print(meta)'''

saldo_positivo = saldo > 0
despesas_controlada = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controlada
print(meta)
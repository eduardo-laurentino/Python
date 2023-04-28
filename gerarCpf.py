cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digit_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digit_1 if digit_1 <= 9 else 0

dez_digitos = nove_digitos + str(digit_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digit_2 = ((resultado_digito_2) * 10 % 11)
digito_2 = digit_2 if digit_2 <= 9 else 0

cpf_calculado = f'{nove_digitos}{digit_1}{digit_2}'
if cpf_enviado_usuario == cpf_calculado:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print("CPF inválido")

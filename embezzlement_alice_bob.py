############## INSIRA O n AQUI ##############
n = 2

lista_de_n = list(range(1, n+1))
binary_state = [0, 0, 1, 1]  # \ket{_0,_0} + \ket{_1,_1}

values = []
for i in lista_de_n:
    n_state = [i, i, i, i]  # \ket{i_,i_} + \ket{i_,i_}
    estado_prensado = [f"{a}{b}" for a, b in zip(n_state, binary_state)]  # \ket{i0,i0} + \ket{i1,i1}
    values.append(estado_prensado)

# Quebrando em listas menores \ket{i0,i0}
values_separados = [
    [sub[i:i+2]
     for i in range(0, len(sub), 2)]
    for sub in values
]

# Adicionando o valor de cada n da lista na frente
values_indiciados = [
    [i, v] for i, v in zip(lista_de_n, values_separados)
]

# Implementação nova de alpha e beta
alpha_beta = [0, 1]
values_alpha_beta = []

for alpha in alpha_beta:
    camada = []
    simbolo = 'a' if alpha == 0 else 'b'  # define o símbolo conforme alpha
    for bloco in values_indiciados:
        n_val, pares = bloco
        # adiciona o símbolo e o par
        novos_pares = [[simbolo, [f"{alpha}{a}", b]] for a, b in pares]
        camada.append([n_val, novos_pares])
    values_alpha_beta.append(camada)

# print(values_alpha_beta)




############### LATEX #######################

def frac(x, y):
    return f"\\dfrac{{{x}}}{{{y}}}"

def sqrt(x):
    return f"\\sqrt{{{x}}}"

def H(x):
    return f"H_{{{x}}}"

def ket(x):
    return f"\\ket{{{x}}}"

def alpha():
    return f"\\alpha"

def beta():
    return f"\\beta"

def soma(x):
    return f"\\left({{{x}}}\\right)"




def gerar_latex(values_alpha_beta):
    termos = []

    for camada in values_alpha_beta:  # percorre alpha e beta


        for bloco in camada:  # percorre cada n_val
            n_val, pares = bloco



            
            for par in pares:  # percorre cada par interno
                simbolo, estados = par
                # Gera o termo com frac e ket
                termo = f"\\frac{{{simbolo}}}{{{sqrt(n_val)}}}{ket(estados[0]+','+estados[1])}"
                termos.append(termo)

    # Junta todos os termos com + dentro de \left( ... \right)
    resultado = "\\left(\n" + "+\n".join(termos) + "\n\\right)"
    return resultado

latex_str = gerar_latex(values_alpha_beta)
print(latex_str)

from math import gcd
############## INSIRA O n AQUI ##############
n = 3

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



# Sqrt term
master = [
    [1, i, v] for i, v in zip(lista_de_n, values_separados)
]





# Guide list: master
print("Guide list = ",master,"\n")




# Latex definitions
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



# Operation module
contador = 0
def mainprint(values_alpha_beta):

    for i in master:
        # i[0] = numerator
        # i[1] = denominator
        ############ OPERATION HERE ############
        i[0] = i[0] 
        i[1] = i[1]


        num = i[0] * 2
        den = i[1]
        m = gcd(num, den)
        num_simpl = num // m
        den_simpl = den // m

        i[0] = num_simpl
        i[1] = den_simpl
        ############ OPERATION HERE ############
    return master









# Modified List: alter
alter = mainprint(master)
print("Modified List =",alter,"\n")




# Print module
def gerar_latex(master):
    termos = []

    for constante, n_val, pares in master:
        for a, b in pares:

            estados = a + ',' + b

            # Conditional 
            if constante == n_val:
                termo = f"{ket(estados)}"
            else:
                termo = f"\\frac{{{sqrt(constante)}}}{{{sqrt(n_val)}}}{ket(estados)}"

            termos.append(termo)

    resultado = "\\left(\n" + "+\n".join(termos) + "\n\\right)"
    return resultado

print("Latex \n\n",gerar_latex(alter))


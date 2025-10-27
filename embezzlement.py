import re

def frac(x, y):
    return f"\\dfrac{{{x}}}{{{y}}}"

def sqrt(x):
    return f"\\sqrt{{{x}}}"

def H(x):
    return f"H_{{{x}}}"

def ket(x):
    return f"\\ket{{{x}}}"



def soma(x):
    lista = [1,2,3,4,5]
    aberto = []
    for x in lista:
        aberto.append(f"{x}") 
    aberto = "+".join(aberto)
    return aberto

print(soma(5))



# f"\\left({{{x}}}\\right)"
'''
print(

    frac(1,sqrt(H(5)))
    +
    soma(


        frac(1,sqrt(1))
        +
        ket("11,11")
        +"+"+
        

        frac(1,sqrt(2))
        +
        ket("10,10")
        +"+"+


        frac(1,sqrt(3))
        +
        ket("21,21")
        +"+"+


        frac(1,sqrt(4))
        +
        ket("20,20")
        +"+"+


        frac(1,sqrt(5))
        +
        ket("31,31")


    )
)



'''

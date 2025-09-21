def frac(x, y):
    return f"\\frac{{{x}}}{{{y}}}"

def sqrt(x):
    return f"\\sqrt{{{x}}}"

def ket(x):
    return f"\\ket{{{x}}}"

def expression(vars):

    terms = []
    for i, k in vars:
        terms.append(f"{frac(1, sqrt(i))}{ket(k)}")
    return f"{frac(1, sqrt('H_5'))}\\left({'+'.join(terms)}\\right)"
vars=[]

def generate(n):
    vars=[]
    for i in range(1,n+1):
        k = (i+1)//2
        if i%2==1:
            valor = f"{k}1,{k}1"
        else:
            valor = f"{k}0,{k}0"
        vars.append((i, valor))
    return vars

n=5

vars=generate(n)

latex_str = expression(vars)
print(latex_str)
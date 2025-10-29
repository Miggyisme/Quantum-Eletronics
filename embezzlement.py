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

n=5

def somaboa(x):
    ns=list(range(n+1))
    return 




print(

    frac(1,sqrt(H(5)))
    +
    soma(

        alpha()+
        frac(1,sqrt(1))
        +
        ket("11,11")
        +"+"+
        
        alpha()+
        frac(1,sqrt(2))
        +
        ket("10,10")
        +"+"+

        alpha()+
        frac(1,sqrt(3))
        +
        ket("21,21")
        +"+"+

        alpha()+
        frac(1,sqrt(4))
        +
        ket("20,20")
        +"+"+

        alpha()+
        frac(1,sqrt(5))
        +
        ket("31,31")


    )
)

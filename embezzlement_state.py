######### Insert the n number #########
n = 4

from math import gcd

def sqrt_tex(x):
    return f"\\sqrt{{{x}}}"

def ket(x):
    return f"\\ket{{{x},{x}}}"


def generate_states(n):

    states = []

    if n >= 1:
        states.append("11")
    if n >= 2:
        states.append("10")

    i = 2
    k = 3

    while k <= n:
        states.append(f"{i}1")
        k += 1
        if k > n:
            break

        states.append(f"{i}0")
        k += 1
        i += 1

    return states


states = generate_states(n)

master = []
for k, state in enumerate(states, start=1):
    master.append([1, k, [[state, state]]])

print("Guide list (master) =\n", master, "\n")


def apply_operations(master_list):
    for i in master_list:

        ###### Operation Module ######
        # i[0] numerator
        # i[1] denominator
        i[0] = i[0]
        i[1] = i[1]

        # Fraction simplification
        m = gcd(i[0], i[1])
        i[0] //= m
        i[1] //= m

        ###### Operation Module ######

    return master_list


alter = apply_operations(master)
print("Modified List =\n", alter, "\n")



# Latex Module
def generate_latex(master_list, n):

    terms = []

    for numerator, denominator, pair in master_list:
        state = pair[0][0]

        num = numerator
        den = denominator

        # If sqrt(1)/sqrt(1), print only the ket
        if num == 1 and den == 1:
            term = ket(state)
        else:
            term = f"\\frac{{{sqrt_tex(num)}}}{{{sqrt_tex(den)}}}{ket(state)}"

        terms.append(term)

    # Mandatory prefix
    prefix = f"U_A U_B \\ket{{\\mu({n})}}\\ket{{00}} = cte"

    return prefix + "\\left(\n" + "+\n".join(terms) + "\n\\right)"


print("Latex final:\n")
print(generate_latex(alter, n))

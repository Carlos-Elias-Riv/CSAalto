def b(b: str):
    if b == 'tr':
        return 0.01
    else:
        return 0.99

def wdadoa(w: str, a: str):
    if w == "tr" and a == "tr":
        return 0.9
    elif w == "fa" and a == "tr":
        return 0.1
    elif w == "tr" and a == "fa":
        return 0.5
    else:
        return 0.5

def gdadoa(g: str, a: str):
    if g == "tr" and a == "tr":
        return 0.7
    elif g == "fa" and a == "tr":
        return 0.3
    elif g == "tr" and a == "fa":
        return 0.2
    else:
        return 0.8

def adadob(a: str, b: str):
    if a == "tr" and b == "tr":
        return 0.99
    elif a == "fa" and b == "tr":
        return 0.01
    elif a == "tr" and b == "fa":
        return 0.05
    else:
        return 0.95

omega = ["tr", "fa"]

# P(B = tr | W = tr)

# P(B = tr, W = tr, A = a, G = g)
numerator = 0

# P(W = tr, A = a, G = g, B = b)
denominator = 0

for g in omega:
    for a in omega:
        numerator += b("tr")*wdadoa("tr", a)*gdadoa(g, a)*adadob(a, "tr")

for g in omega:
    for a in omega:
        for bchica in omega:
            denominator += wdadoa("tr", a)*gdadoa(g, a)*adadob(a, b)*b(bchica)

print(f'Numerador: {numerator}, Denominador: {denominator}, Resultado: {numerator/denominator}')
# alternativamente podemos hacer:

denominator = 0      
for a in omega:
    for bchica in omega:
        denominator += wdadoa("tr", a)*adadob(a, bchica)

print(f'Numerador: {numerator}, Denominador: {denominator}, Resultado: {numerator/denominator}')

# P(B = tr | W = tr, G = fa)

numerator = 0
for a in omega: 
    print(b("tr"), wdadoa("tr", a), gdadoa("fa", a), adadob(a, "tr"))
    numerator += b("tr")*wdadoa("tr", a)*gdadoa("fa", a)*adadob(a, "tr")

denominator = 0

for a in omega:
    for bchica in omega:
        print(b(bchica), wdadoa("tr", a), gdadoa("fa", a), adadob(a, bchica))  
        denominator += wdadoa("tr", a)*gdadoa("fa", a)*adadob(a, bchica)*b(bchica)

print(f'Numerador: {numerator}, Denominador: {denominator}, Resultado: {numerator/denominator}')

# =============================================================================
# Dijkstrov algoritem odstavnega tira
#
# Na predavanjih ste spoznali algoritem za izračun vrednosti aritmetičnega
# izraza, ki uporablja dva sklada: enega za vrednosti, drugega za operacije.
# Z nekaj prilagoditvami lahko ta algoritem pretvorimo v Dijkstrov
# [algoritem odstavnega tira](https://en.wikipedia.org/wiki/Shunting-yard_algorithm),
# ki upošteva tudi prednost operacij, zato nam v aritmetičnem izrazu ni treba
# pisati vseh oklepajev.
# 
# V spodnjih nalogah bomo aritmetične izraze predstavili z nizi, v katerih
# bodo členi ločeni z vsaj enim presledkom, operacije pa bomo omejili na
# `+`, `*` in `**`.
# =====================================================================@010888=
# 1. podnaloga
# Najprej potrebujemo dve pomožni funkciji:
# 
# - `cleni_izraza(izraz)`, ki niz `izraz` po presledkih razbije na člene, ter
# - `izracunaj(a, op, b)`, ki operacijo `op` uporabi na številih `a` in `b`.
# 
#     >>> cleni_izraza(' ( 2 + 4 ) + 6 ')
#     ['(', '2', '+', '4', ')', '+', '6']
#     >>> izracunaj(2, '+', 4)
#     6
#     >>> izracunaj(2, '**', 4)
#     16
# =============================================================================

def cleni_izraza(izraz):
    return izraz.strip().split()

def izracunaj(a,op,b):
    if op == '+':
        return a+b
    elif op == '*':
        return a*b
    elif op=='**':
        return a**b

def izracunaj_v1(a,op,b):
    return {'**': a ** b, '*': a * b, '+': a + b}.get(op,None)

# =====================================================================@010889=
# 2. podnaloga
# Pogost korak pri algoritmu je, da s sklada operacij poberemo operacijo
# (predstavljeno z nizom), s sklada vrednosti dve vrednosti (predstavljeni s
# števili), nato pa na sklad vrednosti vrnemo vrednost izračuna (prestavljeno
# s številom). Sestavite funkcijo `izvedi_racun(sklad_operacij, sklad_vrednosti)`,
# ki izvede zgornji korak.
# 
#     >>> sklad_operacij = Sklad()
#     >>> sklad_vrednosti = Sklad()
#     >>> sklad_vrednosti.vstavi(1)
#     >>> sklad_vrednosti.vstavi(2)
#     >>> sklad_vrednosti.vstavi(3)
#     >>> sklad_operacij.vstavi('+')
#     >>> sklad_operacij.vstavi('*')
#     >>> print(sklad_operacij)
#     DNO : + : * : VRH
#     >>> print(sklad_vrednosti)
#     DNO : 1 : 2 : 3 : VRH
#     >>> izvedi_racun(sklad_operacij, sklad_vrednosti)
#     >>> print(sklad_operacij)
#     DNO : + : VRH
#     >>> print(sklad_vrednosti)
#     DNO : 1 : 6 : VRH
#     >>> izvedi_racun(sklad_operacij, sklad_vrednosti)
#     >>> print(sklad_operacij)
#     DNO : VRH
#     >>> print(sklad_vrednosti)
#     DNO : 7 : VRH
# =============================================================================

from sklad import Sklad
def izvedi_racun(sklad_operacij,sklad_vrednosti):
    '''izvede operacijo na skladu'''
    op = sklad_operacij.vrh()
    sklad_operacij.odstrani()
    b = sklad_vrednosti.vrh()
    sklad_vrednosti.odstrani()
    a = sklad_vrednosti.vrh()
    sklad_vrednosti.odstrani()
    rez = izracunaj(a,op,b)
    sklad_vrednosti.vstavi(rez)
    

# =====================================================================@010886=
# 3. podnaloga
# Za začetek si oglejmo enostaven primer, ko so vsi podizrazi v oklepajih in
# dvoma glede vrstnega reda operacij ni. Sestavite funkcijo
# `vrednost_z_vsemi_oklepaji(izraz)`, ki izračuna in vrne vrednost izraza,
# predstavljenega z nizom `izraz`, zapisanega v običajni obliki z vsemi
# oklepaji. Pri tem sledite algoritmu s predavanj.
# 
#     >>> vrednost_z_vsemi_oklepaji('( 2 + 4 )')
#     6
#     >>> vrednost_z_vsemi_oklepaji('( ( 10 + 5 ) * ( 3 + 7 ) )')
#     150
# =============================================================================

def vrednost_z_vsemi_oklepaji(izraz):
    sklad_vrednosti = Sklad()
    sklad_operacij = Sklad()
    for znak in cleni_izraza(izraz):
        if znak in {'+','*','**'}:
            sklad_operacij.vstavi(znak)
        elif znak.isdigit():
            sklad_vrednosti.vstavi(int(znak))
        elif znak == ')':
            izvedi_racun(sklad_operacij,sklad_vrednosti)
    return sklad_vrednosti.vrh()
    # pregledujemo izraz:
        # ko naletimo na vrednost:
            # jo damo na sklad vrednosti
        # ko naletimo na operator:
            # ga damo na sklad operatorjev
        # ko naletimo na oklepaj:
            # ga preskočimo
        # ko naletimo na zaklepaj:
            # izvedemo račun
# =====================================================================@010890=
# 4. podnaloga
# Glavna razlika med zgornjim in Dijkstrovim algoritmom je, da račune izvedemo
# tudi takrat, ko naletimo na operator, ki nima prednosti.
# 
# Sestavite funkcijo `sklad_ima_prednost(sklad_operacij, op)`, ki vrne `True`,
# kadar je na skladu operacij levo asociativna operacija, ki ima prioriteto
# višjo ali enako operatorju `op`.
# 
#     >>> sklad_operacij = Sklad()
#     >>> print(sklad_ima_prednost(sklad_operacij, '+'))
#     >>> False
#     >>> sklad_operacij.vstavi('*')
#     >>> print(sklad_ima_prednost(sklad_operacij, '*'))
#     >>> True
#     >>> print(sklad_ima_prednost(sklad_operacij, '**'))
#     >>> False
#     >>> sklad_operacij.vstavi('**')
#     >>> print(sklad_ima_prednost(sklad_operacij, '+'))
#     >>> False
# =============================================================================

def sklad_ima_prednost(sklad_operacij, op):
    '''Vrne True, kadar je na skladu operacij levo asc op, ki ima prioriteto višjo ali enako op'''
    if not sklad_operacij.prazen():
        return (op, sklad_operacij.vrh()) in {('*','*'),('+','+'),('+','*')}
    else:
        return False
    

    

# =====================================================================@010887=
# 5. podnaloga
# Sestavite funkcijo `vrednost(izraz)`, ki izračuna in vrne vrednost izraza,
# predstavljenega z nizom `izraz`. Pri tem lahko sledite algoritmu, opisanemu na
# <https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail>.
# 
#     >>> vrednost('( 2 + 4 ) * 3')
#     18
#     >>> vrednost('2 + 4 * 3')
#     14
#     >>> vrednost('2 * 4 + 3')
#     11
# =============================================================================

def vrednost(izraz):
    '''while there are tokens to be read:
	read a token.
	if the token is a number, then push it to the output queue.
	if the token is an operator, then:
		while there is an operator at the top of the operator stack with
			greater than or equal to precedence and the operator is left associative:
				pop operators from the operator stack, onto the output queue.
		push the read operator onto the operator stack.
	if the token is a left bracket (i.e. "("), then:
		push it onto the operator stack.
	if the token is a right bracket (i.e. ")"), then:
		while the operator at the top of the operator stack is not a left bracket:
			pop operators from the operator stack onto the output queue.
		pop the left bracket from the stack.
		/* if the stack runs out without finding a left bracket, then there are
		mismatched parentheses. */
    if there are no more tokens to read:
	while there are still operator tokens on the stack:
		/* if the operator token on the top of the stack is a bracket, then
		there are mismatched parentheses. */
		pop the operator onto the output queue.
    exit.'''
    sklad_operacij,sklad_vrednosti  = Sklad(),Sklad()
    for znak in cleni_izraza(izraz):
        if znak.isdigit():
            sklad_vrednosti.vstavi(int(znak))
        elif znak in {'+','*','**'}:
            while sklad_ima_prednost(sklad_operacij, znak):
                izvedi_racun(sklad_operacij, sklad_vrednosti)
            sklad_operacij.vstavi(znak)
        elif znak == '(':
            sklad_operacij.vstavi(znak)
        elif znak == ')':
            while sklad_operacij.vrh() != '(':
                izvedi_racun(sklad_operacij, sklad_vrednosti)
            sklad_operacij.odstrani()
    while not sklad_operacij.prazen():
        izvedi_racun(sklad_operacij, sklad_vrednosti)
    return sklad_vrednosti.vrh()


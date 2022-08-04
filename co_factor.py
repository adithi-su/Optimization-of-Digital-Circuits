#program to display the co-factors, boolean difference, consensus and smoothing
N = int(input("Enter the number of variables - "))
v = []
for i in range(N): 
    v.append(input())
n = int(input("Enter the number of cubes - "))
cover = []
for i in range(n): 
    cover.append(input())
print("you have entered:", end = '')
print(*cover, sep='+')

# cofactors list = [fa, fa', fb, fb',...]
cof = {}
for var in v:
    temp = var + '\''
    f = []
    f_temp = []
    for i in cover:
        # fa
        if temp not in i:
            if var not in i:
                f.append(i)
            else:
                f.append(i.translate({ord(var): None}))
        if f == '':
            f = 0
        # fa'
        if temp in i:
            f_temp.append(i.replace(temp,''))
        if var not in i:
            f_temp.append(i)
        if f_temp == '':
            f_temp = 0
    cof[var] = f
    cof[temp] = f_temp
    '''print('f',var,end = '= ')
    print(*f, sep='+')
    print('f',temp,end = '= ')
    print(*f_temp, sep='+')'''

print(cof)

#PART 2
x = input('enter the variable to find BOOLEAN DIFFERENCE, CONSENSUS and SMOOTHING-')
x_bar = x + '\''
fx = cof[x]
fx_bar = cof[x_bar]

# Boolean difference = df/dx = fx xor fx'
boo_dif = 1
if fx == fx_bar:
    boo_dif = 0
print('boolean difference wrt', x, '= ', boo_dif)

# Consensus = Cx(f) = fx . fx'
print('consensus wrt',x,'= ',end='(')
print(*fx, sep='+',end=').(')
print(*fx_bar, sep='+', end=')\n')

#Smoothing = Sx(f) = fx + fx'
print('smoothing wrt',x,'= ',end='')
sm = []
for i in fx:
    sm.append(i)
for i in fx_bar:
    if i not in fx:
        sm.append(i)
print(*sm, sep='+')

''' PENDING:
- optimize consensus and smoothing by finding a means to apply boolean laws for computation
'''

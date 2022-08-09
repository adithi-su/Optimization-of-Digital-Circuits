N = int(input("Enter the number of variables, followed by the variables- "))
v = []
for i in range(N): 
    v.append(input())
n = int(input("Enter the number of cubes - "))
cover = []
for i in range(n): 
    cover.append(input())
print("you have entered:", end = '')
print(*cover, sep='+')

# PART 1
# cofactors dictionary wrt variable = {a: fa, a': fa', b: fb, b': fb',...}

def make_cof(v,cover):
    cof = {}
    for var in v:
        temp = var + '\''
        f = []
        f_temp = []
        for i in cover:
            # fa
            if i==var:
                f.append(1)
            else:
                if temp not in i:
                    if var not in i:
                        f.append(i)
                    else:
                        f.append(i.translate({ord(var): None}))
                if f == []:
                    f.append(0)
            # fa'
            if i==temp:
                f_temp.append(1)
            else:
                if temp in i:
                    f_temp.append(i.replace(temp,''))
                if var not in i:
                    f_temp.append(i)
                if f_temp == []:
                    f_temp.append(0)
        cof[var] = f
        cof[temp] = f_temp
    return cof

# user input 
cof = make_cof(v,cover)
print(cof)
v_cof = input('Variable(s) to find co-factor wrt?')
if len(v_cof)==1 or (len(v_cof)==2 and v_cof[1]=='\''):
    print('f',v_cof, '=', end='')
    print(*cof[v_cof], sep='+')
else:
    curr_cof = cof
    curr_cov = cover
    for i in range(len(v_cof)):
        curr_cof = make_cof(v,curr_cov) 
        curr_cov = curr_cof[v_cof[i]]
    print('f',v_cof, '=', end='')
    print(*curr_cov, sep='+')

# PART 2
x = input('enter the variable to find BOOLEAN DIFFERENCE, CONSENSUS and SMOOTHING-')
if len(x) == 1:
    x_bar = x + '\''
elif len(x)==2 and x[1]=='\'':
    x_bar = x[0]
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
Cx_f = []
for i in fx:
    for j in fx_bar:
        prod = i + j 
        Cx_f.append(prod)

#Smoothing = Sx(f) = fx + fx'
print('smoothing wrt',x,'= ',end='')
sm = []
for i in fx:
    sm.append(i)
for i in fx_bar:
    if i not in fx:
        sm.append(i)
print(*sm, sep='+')

'''
User inputs:
1. Enter the number of variables followed by the variables
Sample input for F = abc + ab’
3
a
b
c
Note: Do not enter a’, b’ and so on in the input, directly include them in step 2.
2. Enter the number of cubes, followed by the cube values
Sample input for F = ab + ca’b
2
ab
ca’b
3. The program will display the user input in SoP form, followed by a dictionary of co- factors in the
form {a: fa, a': fa', b: fb, b': fb’...}
Note: Here, the co-factors are stored in list format, i.e., list of cubes.
4. Option 1: Enter variable w.r.t which you wish to find the co-factor (already evident from the
dictionary) – cofactor will be displayed in SoP form.
Option 2: Enter a string (Ex: ac) w.r.t which you wish to find the co-factor.
5. Enter the variable w.r.t which you wish to find Boolean Difference, Smoothing and Consensus.
- The program will display the non-simplified version of the three.
'''

N = int(input("Enter the number of variables, followed by the variables- "))
v = []
for i in range(N): 
    v.append(input())
n = int(input("Enter the number of cubes - "))
cover = []
for i in range(n): 
    cover.append(input())
print("you have entered: ", end = '')
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
v_cof = input('Variable(s) to find co-factor wrt? ')
if len(v_cof)==1 or (len(v_cof)==2 and v_cof[1]=='\''):
    print('f',v_cof, '=', end='')
    if 1 in cof[v_cof]:
        print('1')
    else:
     print(*cof[v_cof], sep='+')
else:
    curr_cof = cof
    curr_cov = cover
    for i in range(len(v_cof)):
        if v_cof[i] == '\'':
            continue
        if i!=(len(v_cof) - 1) and v_cof[i+1]=='\'':
            index = v_cof[i] + '\''
        else:
            index = v_cof[i]
        curr_cof = make_cof(v,curr_cov) 
        curr_cov = curr_cof[index]
    print('f',v_cof, '=', end='')
    if 1 in curr_cov:
        print('1')
    else:
        print(*curr_cov, sep='+')

# PART 2
x = input('enter the variable to find BOOLEAN DIFFERENCE, CONSENSUS and SMOOTHING- ')
if len(x) == 1:
    x_bar = x + '\''
elif len(x)==2 and x[1]=='\'':
    x_bar = x[0]
fx = cof[x]
fx_bar = cof[x_bar]

if 0 in fx and len(fx)!=1:
    fx.remove(0)
if 0 in fx_bar and len(fx_bar)!=1:
    fx_bar.remove(0)

# Boolean difference = df/dx = fx xor fx'
if fx.sort() == fx_bar.sort(): 
    print('boolean difference wrt',x,'=0',end='')
else: # xor = A'B + AB'
    print('boolean difference wrt',x,'= ',end='(')
    #fx.(fx')'
    print(*fx, sep='+',end=').(')
    print(*fx_bar, sep='+', end=')\' + (')
    #(fx)'.fx'
    print(*fx, sep='+',end=')\'.(')
    print(*fx_bar, sep='+', end=')')

# Consensus = Cx(f) = fx . fx'
print('\nconsensus wrt',x,'= ',end='')
# Cx(f) is the largest cube in f which is independent of variable of x.
Cx_f = []
for i in cover:
    if x not in i:
        Cx_f.append(i)
if 1 in Cx_f:
    print('1') # 1+() = 1
else:
    print(*Cx_f, sep='+')

# Smoothing = Sx(f) = fx + fx'
print('smoothing wrt',x,'= ',end='')
# Smoothing wrt a variable means dropping that variable from the function 
Sx_f = []
for i in cover:
    t_x = x + '\''
    if t_x in i:
        Sx_f.append(i.replace(t_x,''))
    if x in i:
        Sx_f.append(i.replace(x,''))
    else:
        Sx_f.append(i)
if 1 in Sx_f:
    print('1') # 1+() = 1
else:
    print(*Sx_f, sep='+')

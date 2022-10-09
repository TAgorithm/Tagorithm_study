import sys

chemicalf = list(sys.stdin.readline().rstrip())
stack = []

chdict = {'H':1, 'C': 12, 'O':16}

for ch in chemicalf:
    if ch == ')':
        chemicalsum = 0
        while(stack):
            chemical = stack.pop()
            if chemical == '(':
                break
            chemicalsum += chemical
        stack.append(chemicalsum)
    elif ch == '(':
        stack.append(ch)
    elif ch == 'H' or ch == 'O' or ch == 'C':
        stack.append(chdict[ch])
    else:
        stack[-1] *= int(ch)

print(sum(stack))

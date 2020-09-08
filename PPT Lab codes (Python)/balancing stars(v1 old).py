def check(c, l, l1):
    if c == '{' or c == '[' or c == '(':
        if c == '{':
            l[0] = l[0] + 1
            l1[0] = l1[0] + 1
            return l, l1
        if c == '[':
            l[1] = l[1] + 1
            l1[1] = l1[1] + 1
            return l, l1
        if c == '(':
            l[2] = l[2] + 1
            l1[2] = l1[2] + 1
            return l, l1

    elif c == '}' or c == ']' or c == ')':
        if c == '}':
            l[0] = l[0] - 1
            l1[0] = l1[0] + 1
            return l, l1
        if c == ']':
            l[1] = l[1] - 1
            l1[1] = l1[1] + 1
            return l, l1
        if c == ')':
            l[2] = l[2] - 1
            l1[2] = l1[2] + 1
            return l, l1
    return l, l1


string = input()
l = [0, 0, 0]
l1 = [0, 0, 0]
c = 0
flag = 0
for i in range(len(string)):
    l, l1 = check(string[i], l, l1)
    if l[0] < 0 or l[1] < 0 or l[2] < 0:
        flag = 1

x = int(l1[0] / 2) + int(l1[1] / 2) + int(l1[2] / 2)
if flag == 1:
    print("NO ", x)
else:
    print("YES ", x)

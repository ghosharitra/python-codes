def check(c, flag, i, string, x):
    if c == '{' or c == '[' or c == '(':
        if c == '{':
            for j in range(i, len(string)):
                if (string[j] == '}'):
                    string = string[:j] + string[j + 1:]
                    x += 1
                    break
            else:
                flag = 1
            return flag, string, x
        if c == '[':
            for j in range(i, len(string)):
                if (string[j] == ']'):
                    string = string[:j] + string[j + 1:]
                    x += 1
                    break
            else:
                flag = 1
            return flag, string, x
        if c == '(':
            for j in range(i, len(string)):
                if (string[j] == ')'):
                    string = string[:j] + string[j + 1:]
                    x += 1
                    break
            else:
                flag = 1
            return flag, string, x

    elif c == '}' or c == ']' or c == ')':
        flag = 1
        return flag, string, x

    return flag, string, x


string = input()
x = 0
flag = 0
i = 0
while i < len(string):
    flag, string, x = check(string[i], flag, i, string, x)
    # print(string)
    i += 1

if flag == 1:
    print("NO ", x)
else:
    print("YES ", x)
# {)[}(]
# {}{{{}}}())(()][][]}}}]]




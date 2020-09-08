n = int(input("Enter number of Stairs:"))
arr=[-1]*(n+2)
def calc(x):
    print("arr:",arr)
    print("x:",x)
    if(arr[x]!=-1):
        return arr[x]
    if x <= 1:
        arr[x]=x
        return x
    res=calc(x - 1) + calc(x - 2)
    arr[x]=res
    return res


def count(n):
    res=calc(n + 1)
    print("arr=",arr)
    return res


print("Number of ways:", count(n))
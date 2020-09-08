i=1

#main()
# we cant call a function before it is defined


def main():
    global i
    if i<=5:
        i+=1
        print("main")
        fun()

#main()
# we cant call a function (even indirectly) before it is defined. Like here we were calling fun() indirectly before it is defined.


def fun():
    print("fun")
    main()

main()
#even if fun() is defined after main(), main() can still call it as the main() function itself is called after the fun() is defined.

def stringAnagram(dictionary,query):

    dict1={}
    
    for d in dictionary:
        dct={ "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    
        for i in d:
            dct[i]+=1
        
        #print(dct)
        #print("\n\n\n")
        
        l=[]
        for i in dct:
            l.append(dct[i])
        t=tuple(l)


        if(t in dict1):
            dict1[t]+=1
        else:
            dict1[t]=1
        
    for i in dict1:
        print(i,dict1[i])

    res=[]

    for d in query:
        dct={ "a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    
        for i in d:
            dct[i]+=1
        
        # print(dct)
        # print("\n\n\n")
        
        l=[]
        for i in dct:
            l.append(dct[i])
        t=tuple(l)

        if(t in dict1):
            res.append( dict1[t] )
        else:
            res.append(0)

    print(res)
    return res






dictionary=['hack','a','rank','khac','ackh','kran','rankhacker','a','ab','ba','stairs','raits']
query=["a","nark","bs","hack","stair"]
stringAnagram(dictionary,query)

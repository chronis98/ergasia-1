sen=raw_input("dwse protash")
sen=list(sen)
new_sen=[""]*len(sen)
print sen
x=0
for i in range(len(sen)-1):
    flag=0
    if sen[i]=="!":
        k=i+1
        while(k<=len(sen)-1):
            if sen[k]!="!":
                if sen[k].isupper():
                   flag=k
                k=len(sen)
            k+=1
        if flag>0:
                new_sen[x]=sen[i]
                x+=1
    else:
        new_sen[x]=sen[i]
        x+=1
print "arxikh protash xrhsth:","".join(sen)
print "tropopoihmenh protash:","".join(new_sen)

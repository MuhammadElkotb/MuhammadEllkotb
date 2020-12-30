import math
f=True
while(f==True):

        varbs = [ varbs for varbs in input("Enter Variables ").split()]
        varbs=sorted(varbs)
        varb=len(varbs)

        def nobits1(n):
             bits1=0
             for i in n:
                if i=='1':
                    bits1+=1
             return bits1


        minterms =[(int(minterms)) for minterms in input("Enter Minterms ").split()]
        if(max(minterms)!=0):
            if (int(math.log(max(minterms), 2)) >= varb):
                print("Invalid Input Please Try Again")
                continue


        minterms = set(minterms)
        minterms = list(minterms)
        minterms1=[]
        for i in range(len(minterms)):
            minterms1.append(format(minterms[i], '#010b'))




        indexes = [[[] for i in range(max(minterms)+2)] for k in range(varb+1)]


        for i in minterms1:
            indexes[0][nobits1(i)].append(i)
        ctr=0
        notpi=[]
        pi=[]
        for i in range(len(indexes)):
            if (i == 2):
                break
            for j in range(len(indexes[i])):
                for k in range(len(indexes[i][j])):
                    for t in range(len(indexes[i][j+1])):
                        for m in range(10):
                            if(indexes[i][j][k][m]!=indexes[i][j+1][t][m]):
                                ctr+=1
                                u=m
                        if(ctr==1):
                            notpi.append(indexes[i][j][k])
                            notpi.append(indexes[i][j + 1][t])
                            notpi=set(notpi)
                            notpi=list(notpi)
                            yy=list(indexes[i][j][k])
                            yy[u]='-'
                            yy=''.join(yy)
                            indexes[i+1][j].append(yy)
                            ctr = 0
                        ctr=0
                    ctr=0
                ctr=0
            ctr=0


        for i in range(len(indexes)):
            for j in range(len(indexes[i])):
                    for k in indexes[i][j]:
                        if(k not in notpi):
                            pi.append(k)


        pi=set(pi)
        pi=list(pi)
        print(notpi, '\n')
        #print(indexes)
        #print(minterms1)

        print([pi], '\n')


        for i in range(len(pi)):
            pi[i]=list(pi[i])
            del pi[i][0:(10-varb)]
            for j in range(varb):
                if(pi[i][j]=='0'):
                    pi[i][j] = varbs[j] + '`'
                if(pi[i][j]=='1'):
                    pi[i][j]=varbs[j]

            for l in range(varb):
                if(pi[i][l]=='-'):
                    pi[i][l]=''
            pi[i]=''.join(pi[i])


        pi=set(pi)
        pi=list(pi)
        pi=sorted(pi)
        print("Prime Implicants -->> ", '\n')
        for i in pi:
            print(i, '\n')


        ff=input("To END Press '0'    To RESET Press '1' .....")

        if(ff=='0'):
            f=False
        else:
            continue



















#64	10 01

###s0
oper, f, s = input().split() #y1y2y3
sost = "s0"
err = "000"
ans = 0#y6
###


def printEnv():
    print("ERROR CODE:", err)#y7
    print("S:", sost)#y8
    print("FIRST OP:", f)#y9
    print("SECOND OP:", s)#y10
    print("OPERATION:", oper)#y11
    print("ANSWER:", bin(int(ans))[2::].zfill(64))#y12
    print()#y13


def validate():
    global err, f, s,sost #y14y15y16y17
    if(len(f) < 64 or len(s) < 64 or len(s) != len(f)): ##X1
        err = "001" #y18
        printEnv()######
        #####S0
        exit(0)
        #####S0
    if(len(f) > 64 or len(s) > 64):
        err = "010"
        printEnv()
        exit(0)
    if f.count('0') + f.count('1') != len(f) or s.count('0') + s.count('1') != len(s):
        err = "011"
        printEnv()
        exit(0)

def sim():
    global err,ans, oper, sost
    if oper == "10":
        if int(s, 2) == 0:
            err = "100"
            printEnv()
            exit(0)
        ans = int(f, 2) / int(s, 2)
        if(len(bin(int(ans))[2::]) > 64):
            err = '101'
            printEnv()
            exit(0)
        printEnv()
        exit(0)
    elif oper == "01":
        ans = int(f, 2) * int(s, 2)
        if (len(bin(ans)[2::]) > 64):
            err = '101'
            printEnv()
            exit(0)
        printEnv()
        exit(0)
    else:
        err = "110"
        printEnv()
        exit(0)
##S1
printEnv()
######

####S2
validate()
#######
sim()






#64	10 01
oper, f, s = input().split()
sost = "s0"
err = "000"
ans = 0
print(sost)
print(oper,f,s,err,sep='\n')

if(len(f) < 64 or len(s) < 64 or len(s) != len(f)):
    err = "100"
    print("ERROR CODE:",err)
    print("SOST:",sost)
    exit(0)
if(len(f) > 64 or len(s) > 64):
    err = "101"
    print("ERROR CODE:", err)
    print("SOST: ", sost)
    exit(0)
if f.count("0")+f.count("1") != len(f) or s.count("0")+s.count("1") != len(s):
    err = "011"
    print("ERROR CODE:", err)
    print("SOST:", sost)
    exit(0)

if oper == "10":
    if int (s,2) == 0:
        err = "001"
        print("ERROR CODE:", err)
        print("SOST:", sost)
        exit(0)
    ans = int(f,2) / int(s,2)
    print("ERROR CODE:", err)
    print("SOST:", sost)
    print("FIRST OP:", f)
    print("SECOND OP:", s)
    print("OPERATIONS:", oper)
    print("ANSWER:", ans)
    exit(0)


elif oper == "01":
    ans = int(f,2) * int(s,2)
    print("ERROR CODE:", err)
    print("SOST:", sost)
    print("FIRST OP:", f)
    print("SECOND OP:", s)
    print("OPERATIONS:", oper)
    print("ANSWER:", ans)
    exit(0)




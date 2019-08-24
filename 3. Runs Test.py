import math

def runstest(data):
    V = 1
    for i in range(int(len(data)-1)):
        if data[i]!=data[i+1] :
            V=V+1
        elif data[int(len(data)-1)]!=data[int(len(data)-2)]:
            V = V+1
        else:
            pass
    n = 0
    for j in range(len(data)):
        if data[j]=="1":
            n = n + 1
    m = float(n)/len(data)
    t = 2.0/math.sqrt(len(data))
    #print t
    u = abs(float(m-0.5))
    if u<t :
        a = float(V - (2*int(len(data))*m*(1-m)))
        b = (2*math.sqrt(2*int(len(data)))*m*(1-m))
        print a,b
        pvalue = math.erfc((float(abs(a))/(b)))
        print "P-value of the given sequence is : ",pvalue
        if pvalue > 0.01:
            print "PASS"
        else:
            print "FAIL"
    else:
        print "FAIL"

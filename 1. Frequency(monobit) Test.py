import math

def frequencytest(data):
    e = list()
    s = 0
    for i in range(len(data)):
        e.append(int(2*int(data[i])) - 1)
    for j in range(len(e)):
        s = s + e[j]
    value = float(s)/math.sqrt(2*int(len(e)))
    pvalue = math.erfc(abs(value))
    #print value
    print ("P-value of the given sequence is : ",pvalue)
    if pvalue > 0.01:
        return "PASS"
    else:
        return "FAIL"

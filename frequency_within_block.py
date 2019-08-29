import math
from scipy.special import gammaincc

def frequencywithinblock(data , blocklen):
    number_of_blocks = math.floor(len(data)/blocklen)
    pi = list()
    #Determine the proportion πi of ones in each M-bit block
    for i in range(1,number_of_blocks+1):
        pii=0
        for j in range(0,blocklen):
            pii =pii + (int((data[((i-1)*blocklen + j)]))/blocklen)
        pi.append(pii)
    #Compute the chisq statistic
    chisq = 0
    for i in range(0,number_of_blocks):
        chisq = float(chisq) + float((pi[i]-0.5)**2)
    chisq = 4*blocklen*chisq
    #p-value
    pvalue = scipy.special.gammaincc(number_of_blocks/2 , chisq/2)
    print(pvalue)
    if pvalue>0.01:
        return "Pass"
    else:
        return "Fail"

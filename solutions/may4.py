class Solution:
    def findComplement(self, num: int) -> int:
        f=''
        n = False
        for i in str(bin(num)):
            if (i=='1' and n is True):
                f+='0'
            elif (i=='0' and n==True):
                f+='1'
            elif i=='b':
                n = True
        return(int(f,2))

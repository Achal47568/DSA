class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]  
        #binary output in form: 0b ,so: [2:] removes 0b
        #(a,2)  base 2 for binary
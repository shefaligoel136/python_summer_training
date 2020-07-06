#https://practice.geeksforgeeks.org/contest-problem/deep-copy-objects/1/

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        b=int(input())
        c=int(input())
        
        r1=Cuboid(a,b,c)
        r2=Cuboid(a,b,c)
        
        r2.deepCopy(r1)
        
        r2.increaseDimensions()
        r2.increaseDimensions()
        r1.increaseDimensions()
        
        print(r1.getArea(),r2.getArea())
        
        testcases-=1
        
if __name__=='__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
class Cuboid:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def getArea(self):
        return self.l*self.h*self.b
    def increaseDimensions(self):
        self.l=self.l+1
        self.b=self.b+1
        self.h=self.h+1
    def deepCopy(self,obj):
        self = obj

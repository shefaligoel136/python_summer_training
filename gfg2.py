"""https://practice.geeksforgeeks.org/contest-problem/fibonacci-objects/1/"""

{
#Initial Template for Python 3
class FibO:
    def _init_(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def fiboSum(self,obj):
        self.x+=obj.x
        self.y+=obj.y
        self.z+=obj.z
    def getCoord(self):
        print(self.x,self.y,self.z)
    def deepCopy(self,obj):
        self.x,self.y,self.z=obj.x,obj.y,obj.z
        
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        
        xyz1=[int(i) for i in input().split()]
        x1=xyz1[0]
        y1=xyz1[1]
        z1=xyz1[2]
        
        xyz2=[int(i) for i in input().split()]
        x2=xyz2[0]
        y2=xyz2[1]
        z2=xyz2[2]
        
        n=int(input())
        obj1=FibO(x1,y1,z1)
        obj2=FibO(x2,y2,z2)
        (nthFibO(n,obj1,obj2).getCoord())
        
        testcases-=1
        
if _name=='main_':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def nthFibO(n,a,b):
 if(n==1):
        return a
    if(n==2):
        return b
    temp=FibO(1,1,1)
    for i in range(3,n+1):
        temp.deepCopy(b);
        b.fiboSum(a)
        a.deepCopy(temp)
    return b


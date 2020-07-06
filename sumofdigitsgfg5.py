{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        
if __name__=='__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def digitsSum(n):
  num = map(int,list(str(n)))
  return(sum(num))
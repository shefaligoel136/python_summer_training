{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        ##input object1
        name1=input()
        hp1=int(input())
        boost1=int(input())
        ##input object2
        name2=input()
        hp2=int(input())
        boost2=int(input())
        ##creating objects 1 and 2
        chara1=Character(name1,hp1)
        chara1.boost(boost1)
        
        chara2=Character(name2,hp2)
        chara2.boost(boost2)
        ##fuse and show the result
        show(fusion(chara1,chara2))
        testcases-=1
        
if __name__=='__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
class Character:
    def __init__(self,name,hp):
        self.name=name ##Assigning name to the current object's name variable
        self.hp=hp ##Assigning hp to the current object's hp variable
    def boost(self,amount):
        self.hp=self.hp*amount ## boosting current object's hp
    def getName(self):
        return self.name
    def getHp(self):
        return self.hp
def fusion(a,b):
    l1 = int(len(a.name)/2)
    l2 = int(len(b.name)/2)
    s  = a.name[:l1]+b.name[l2:]  
    hp = a.hp+b.hp
    r = Character(s,hp)
    return r


def show(a): ##Already completed
    print(a.getName(),a.getHp()) ##printing the newobject's name and hp





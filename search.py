#i have built a proof searcher. 'rules' contain all the dummy inference rules (for now)
#there can be bugs

import sys
from collections import deque

#class node:
#    def __init__(self,key):
#        self.key=key
#        self.parent=None
#        self.left=None
#        self.right=None

rules=[]
rules.append(('a1','b1','c2'));
rules.append(('a1','b1','c1','d1'));
rules.append(('b2','d2'));
rules.append(('d2','e2'));
rules.append(('d1','n'));
rules.append(('c1','d2'));
rules.append(('b1','e1','f1','g1','h1'));
rules.append(('c2','f2'));
rules.append(('c1','e1'));
rules.append(('e1','k1','l1'));
rules.append(('h1','i1','j1'));
rules.append(('f1','n'));
rules.append(('k1','n'));
rules.append(('l1','n'));
rules.append(('g1','n'));
rules.append(('h1','n'));
rules.append(('i1','n'));
rules.append(('j1','n'));

def search(k,key):
    if k>=len(rules):
        return -1
    j=k;
    for i in rules[k:]:
        if i[0]==key:
            return j;
        j+=1;

    return -1;

#def disptree(stack1,stack2):


def main():
    fc='a1'
    queue1=deque(['a1']);
    queue2=deque([-1]);
    queue3=deque([0]);
    stack1=[];
    stack2=[];
    stack3=[];
    while queue1:
        if queue1 and all(elem=='n' for elem in queue1):
            print("proof found")
            break;
        x=queue1.popleft();
        x2=queue2.popleft();
        x3=queue3.popleft();
        print x3

        print x
        print '\n'
        i=search(x3,x);
        if x==fc and i==-1:
            print "proof not found"
            break
        stack1.append(x);
        stack2.append(x2);
        stack3.append(i);

        if x=='n':
            continue;


        if i==-1:
            x=stack1.pop();
            k=stack2.pop();
            l=stack3.pop();
            p=rules[k][0];
            m1=rules[k].index(x);
            queue1=deque([]);
            queue2=deque([]);
            queue3=deque([]);
            while stack1:
                m1-=1
                x1=stack1.pop();
                x2=stack2.pop();
                x3=stack3.pop();
                if x1==p:
                    break;
                if m1<=0:
                    queue1.appendleft(x1);
                    queue2.appendleft(x2);
                    queue3.appendleft(x3);
            #queue1=[x1]+queue1;
            #queue2=[x2]+queue2;
            #queue3=[k+1]+queue3;
            queue1.appendleft(x1);
            queue2.appendleft(x2);
            queue3.appendleft(k+1);
            continue;
        y=rules[i];
        for j in y[1:]:
            queue1.append(j);
            queue2.append(i);
            queue3.append(0);

    stack1.reverse()
    stack2.reverse()
    stack2.pop()
    print fc
    while stack2:
        m=stack2.pop()
        t=len(rules[m])
        print rules[m][1:]
        while t-2:
            stack2.pop()
            t-=1

    #while stack1:
    #   print stack1.pop()
#
    #while stack2:
    #    print stack2.pop()


#
#
    #while queue1:
    #    print queue1.popleft();
#
    #while queue2:
    #    print queue2.popleft();
#
    #while queue3:
    #    print queue3.popleft();






if __name__ == '__main__':
    main()

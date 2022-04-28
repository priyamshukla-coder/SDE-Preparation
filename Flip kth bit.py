'''
Question : Flip the kth bit of the number. ( If the bit is 1 set to 0 else it remains same )
T.C. : O(1)
S.C. : O(1)
Concept : Bitwise And

'''

import os,sys

if  os.path.exists('Input.txt'):
    sys.stdin=open('Input.txt', 'r')
    sys.stdout=open('Output.txt', 'w')


n,k=map(int,input().split())
print(n & ~(1<<(k-1)))
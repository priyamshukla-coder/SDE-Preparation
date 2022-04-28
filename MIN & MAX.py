'''
Question : Find Minimum and Maximum without using MIN & MAX function
T.C. : O(1)
S.C. : O(1)
Concept : Basic Maths

'''
import os,sys

if  os.path.exists('Input.txt'):
    sys.stdin=open('Input.txt', 'r')
    sys.stdout=open('Output.txt', 'w')

def cal_min(a,b):
    diff=a-b
    min_res=a+b-abs(diff)
    return min_res//2

def cal_max(a,b):
    diff=a-b
    max_res=a+b+abs(diff)
    return max_res//2

a,b=map(int,input().split())
print(cal_max(a,b),cal_min(a,b))

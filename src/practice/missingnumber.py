'''
Created on 2013-5-17

@author: shunlil
'''

import random

def producearray():
    N = 10
    arr = range(1,N+1) #initialize arr with [1,2,3,4...,N]
    random.shuffle(arr) #randomize order
    r = random.randint(0,N) #pick random r between [0,N)
    arr[r] = 0 # set random element to 0
    #print arr
    return arr

def produce_duplicate_array():
    N = 10
    arr = range(1,N+1) #initialize arr with [1,2,3,4...,N]
    r = random.randint(0,N) #pick random r between [0,N)
    arr1=range(1,N+1)
    arr1.remove(r)
    #print len(arr1)
    arr.extend(arr1)
    random.shuffle(arr) #randomize order
    print arr
    return arr


def missing_number_naive(arr):
    N=len(arr)
    for v in range(1,N+1): # for each v in [1,N]
        if v not in arr: # is v present in arr?
            return v
    return None

def missing_number_linear(arr):
    n=len(arr);
    return n*(n+1)/2 -sum(arr);

def missing_number_bitarray(arr):
    pass
    
def missing_number_xor(arr):
    N=len(arr)
    Q = [N,1,N+1,0][N%4]
    P = 0
    for v in arr:
        P = P ^ v
    return P ^ Q
    
def missing_number_xor_1(arr):
    N=len(arr)
    P = 0
    for v in range(1,N+1):
        P=P^v
    for v in arr:
        P = P ^ v
    return P
    

def sort3number():
    a,b,c = [random.randint(-100,100) for i in range(3)]
    print a,b,c
    mx=max(a,max(b,c))
    mn=-max(-a,max(-b,-c))
    mid=a+b+c-mx-mn
    print mn,mid,mx

def missing_duplicate_number_xor(arr):
    x=0
    for v in arr:
        x=x^v
    return x 
    
    
if __name__ == '__main__':
    arr=producearray()
    print missing_number_naive(arr)
    print missing_number_linear(arr)
    print missing_number_xor(arr)
    print missing_number_xor_1(arr)
    sort3number()
    
    arr=produce_duplicate_array()
    print missing_duplicate_number_xor(arr)
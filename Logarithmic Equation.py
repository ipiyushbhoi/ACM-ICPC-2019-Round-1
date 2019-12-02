
'''
Chef has a sequence of N integers A1,A2,A3,....,An.

Chef thinks that a triplet of integers (i,j,k) is good if 1<=i<j<k<=N and P in the
following expressionn contains an odd number of ones in its binary representation

P=[Ai <<([log2(Aj)] + [log2(Ak)] +2)]+ [Aj <<([log2(Ak)] + 1] +Ak

The << operator is called left shif, x<<y is defined as x.2^y

Help the chef finding the total number of good triplets modulo 10^9+7

Constraints:

1<=T<=1000
1<=N<=100000
1<=Ai<=10^9

The sum of N over all testcase is less than 10^6

Sample Input:

1
4
1 1 2 3

Sample Output:

1
'''



try:
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))

        l=[]
        n=len(a)

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if i!=j and i!=k and k!=i:
                        p=(a[i]<<math.ceil(math.log2(a[j]))+math.ceil(math.log2(a[k]))+2)+(a[j]<<math.ceil(math.log2(a[k]))+1)+a[k]
                        t=bin(p)[2:]
                        l.append(p)



        l=[bin(i)[2:] for i in l]
        l=[countone(i) for i in l]
        l=[i for i in l if i is not 0]
        print(len(l)%1000000007)
        
except:
    pass

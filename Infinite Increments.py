
'''
Chef has a garden with N plants arranged in a line in decreasing order of height.
Initially, the height of the plants are A1,A2,A3,....An.

The plants are growing,after each hour the height of the i-th plant increases by i millimeters.
Find the minimum number of integer hours, that Chef must wait to have two plants of the same height.


Constraints:

1<=T<=1000
2<=N<=100000
0<=A<=10^18
Ai>A(i+1), for each valid i
The sum of N over all testcase is less than 10^6

Sample Input:

1
3
8 4 2

Sample Output:

2

Explanation:

After 2 hours there are two plants with the same height

[8,4,2]->[9,6,5]->[10,8,8]
'''



try:
    
    for _ in range(int(input())):

        n=int(input())
        l=list(map(int,input().split()))
    
    
        l=set(l)

        n=len(l)



        c=0

        while(1):
    
            l=list(l)
            l=[l[i]+i+1 for i in range(len(l))]
            l=set(l)
    
            if len(l)==n-1:
                break
            c+=1
    
        print(c+1) 
        print()

except:
    pass

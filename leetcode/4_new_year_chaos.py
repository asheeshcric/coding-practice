# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    is_chaotic = False
    
    for i in range(len(q)):
        # Check for chaotic
        if q[i] - (i+1) > 2:
            is_chaotic = True
            break
        
        # Count the number of bribes
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                bribes += 1
        
    if is_chaotic:
        print('Too chaotic')
    else:
        print(bribes)
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
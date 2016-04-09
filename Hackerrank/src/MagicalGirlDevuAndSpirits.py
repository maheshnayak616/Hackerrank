import sys
def modify_linear(A):
    max_ending_here = 0
    min_value = 0
    convert = False
    c = 0
    for x in A:
        if x < min_value: min_value = x
        max_ending_here = max_ending_here + x
        if max_ending_here <= 0 and convert == False:
            convert = True
            max_ending_here = max_ending_here - (2 * min_value)
        c = c + 1
        if max_ending_here <= 0:
            break    
    return (c,max_ending_here)

t = int(input())
while t>=0:
    t = t - 1
    l = int(input())
    arr = sys.stdin.readline().strip().split(' ')
    A = [int(x) for x in arr]
    (c,max_ending_here) = modify_linear(A)
#     f = open("/Users/mahesh.nayak/Desktop/answers.txt",'a')
    if max_ending_here >=0 :
#         f.write("She did it!")
#         f.write('\n')
        print "She did it!"
    else:
#         f.write(str(c))
#         f.write('\n')
        print c
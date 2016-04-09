t = int(raw_input().strip())
for a0 in xrange(t):
    B, W = raw_input().strip().split(' ')
    B, W = [int(B), int(W)]
    X, Y, Z = raw_input().strip().split(' ')
    X, Y, Z = [int(X), int(Y), int(Z)]

    cB = Y + Z
    cW = X + Z

    sum = 0
    sum += B * (X if X < cB else cB)
    sum += W * (Y if Y < cW else cW)

    print sum

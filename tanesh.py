def solution(X, Y, D):
    distance = Y - X
    jumps = int(distance / D)
    if distance % D == 0:
        return jumps
    else:
        return jumps + 1

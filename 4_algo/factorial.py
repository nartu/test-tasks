
def factorial(n):
    f = 1
    if n==0 or n==1:
        return f
    for i in range(2,n+1):
        f = f * i
        # print(f)
    return f

def factorial_r(n):
    f = 1
    if n==0:
        print(f"Step: {n}, result: {f}")
        return f
    f = n * factorial_r(n-1)
    print(f"Step: {n}, result: {f}")
    return f


if __name__ == '__main__':
    print(factorial_r(3))

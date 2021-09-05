# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
# Написать функцию возвращающую четные элементы последовательности Фибоначчи.
# Например, f(4) вернет 0,2,8,34


def fib(n):
    a,b = 0,1
    for i in range(n+1):
        if i==0: print(a)
        if i==1: print(b)
        if i>1:
            s = a+b
            print(s)
            a,b = b,s

def fib_even(n):
    a,b = 0,1
    i,j = 0,0
    while j < n:
        if i==0: s = a
        elif i==1: s = b
        else:
            s = a+b
            a,b = b,s
        if s%2==0:
            j += 1
            print(s)
        i += 1

j = 0
def fib_r(n):
    f = 0
    global j   #steps
    if n==0:
        j += 1
        print(f"Step: {j}, n: {n}, result: {f}")
        return 0
    elif n==1:
        j += 1
        print(f"Step: {j}, n: {n}, result: {f}")
        return 1
    else:
        f = fib_r(n-1) + fib_r(n-2)
        j += 1
        print(f"Step: {j}, n: {n}, result: {f}")
        return f




if __name__ == '__main__':
    j = 0
    print(fib_r(5))
    print("---------------------")
    fib(4)

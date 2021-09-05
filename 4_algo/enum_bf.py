step = 0 # for number of function calls
def bf(n, el):
    # all elements of list el, ex. [1,2,3]
    global step
    if n<=1:
        for i in el:
            yield str(i)
    else:
        for j in el:
            for i in bf(n-1, el):
                step += 1
                yield str(j)+i

def dis_odd(n, el):
    for i in bf(n, el):
        etalon = i[0]
        pt = True
        for j in range(len(i)):
            # odd elements is same, even elements is other not like odd
            if j%2==0 and i[j] != etalon or j%2==1 and i[j] == etalon:
                pt = False
                break
        if pt: print(i)

if __name__ == '__main__':
    dis_odd(11, list(range(10)))
    # print(*bf(4, el=[1,2,3,4,5]))
    # print(list(bf(3)))
    print(step)

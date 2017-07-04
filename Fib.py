



def fib1(n): # через цикл
    fib1 = [0, 1]
    for i in range(2,n+1):
        fib1.append(fib1[i-1]+fib1[i-2])
    return fib1[n]
n = int(input('Введите n '))
print(fib1(n))





def fib2(n): # рекурсивно
    if n < 2:
        return n
    else:
        return fib2(n-1)+fib2(n-2)
    
n = int(input('Введите n '))
print(fib2(n))


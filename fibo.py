def recursivve_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursivve_nth_fibo(n - 1) + recursivve_nth_fibo(n-2)

def main():
    n = int(input("Zadejte poradi hledaneho prvku Fibonacciho posloupnosti: "))
    fib_seq = []
    for x in range(n+1):
        fib_seq.append(recursivve_nth_fibo(x))
    print(fib_seq)

if __name__ == '__main__':
    main()

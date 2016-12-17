def fibonacci(n):
    if n == 1:
        return [1]
    f = [1, 1]
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    return f


def fibonacci_rec(n):
    if n <= 2:
        return [1] * n
    s = fibonacci_rec(n - 1)
    return s + [s[-2] + s[-1]]


def fibonacci_diz(n):
    if n == 1:
        return {1: 1}
    fib = {1: 1, 2: 1}
    for x in range(3, n + 1):
        fib[x] = fib[x - 1] + fib[x - 2]
    return fib


def fibonacci_diz_rec(n):
    if n == 1:
        return {1: 1}
    if n == 2:
        return {1: 1, 2: 1}
    # if n <= 2:
    #     return {x: 1 for x in range(1, n + 1)}
    s = fibonacci_diz_rec(n - 1)
    return {**s, **{n: s[n - 1] + s[n - 2]}}


def main():
    functions = [fibonacci, fibonacci_rec, fibonacci_diz, fibonacci_diz_rec]
    for i in range(2, 6):
        for f in functions:
            print(f(i))


if __name__ == '__main__':
    main()

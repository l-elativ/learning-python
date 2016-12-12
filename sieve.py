def sieve(n):
    soe = list(range(2, n))
    # soe = [x for x in range(2, n)]
    primes = []
    while pow(soe[0], 2) <= n:
        primes.append(soe[0])
        soe = [x for x in soe[1:] if x % soe[0] != 0]

        # soe = list(filter(partial(multipli, soe[0]), soe[1:]))

        # for x in soe[1:]:
        #     if x % soe[0] == 0:
        #         soe.remove(x)
        # soe = list(filter(lambda x: x % soe[0] != 0, soe[1:]))
    return primes + soe


def main():
    print(sieve(100))

if __name__ == '__main__':
    main()

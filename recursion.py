def mcd(a, b):
    return mcd(max(a, b) - min(a, b), min(a, b)) if a != b else a
    # if a == b:
    #     return a
    # return mcd(a - b, b) if a > b else mcd(a, b - a)
vxcvcvvcvcxvcx

def main():
    print(mcd(18, 6))

if __name__ == '__main__':
    main()

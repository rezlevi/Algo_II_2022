def power(P):
    if P == 0:
        return 1

    return (2 * power(P - 1))


if __name__ == '__main__':
    P = 2

    print(power(P))
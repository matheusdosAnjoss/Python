def fatorial(n=1, show=True):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x', end=' ')
        f *= c
    return f


print(f'{fatorial(4)}')
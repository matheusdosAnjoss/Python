def dobra(val):
    pos = 0
    while pos < len(val):
        val[pos]*=2
        pos += 1

valores = [4, 6, 3, 7, 2, 5]

print(valores)
dobra(valores)
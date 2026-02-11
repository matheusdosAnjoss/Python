def notas(*n, sit=True):
    """"
    -> fucao para analisar notas e situacoes de varios alunos
    
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIN'
    return r

resp = notas(5.5, 5.5, 8.5)
print(resp)

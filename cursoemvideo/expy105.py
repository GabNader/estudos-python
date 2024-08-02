def notas(*num, sit=False):
    dicio = dict()
    dicio['quant'] = len(num)
    dicio['maior'] = max(num)
    dicio['menor'] = min(num)
    dicio['média'] = sum(num) / (len(num))
    if sit is True:
        if dicio['média'] > 7:
            dicio['situação'] = 'BOA'
        elif 7 > dicio['média'] >= 5:
            dicio['situação'] = 'EXAME'
        else:
            dicio['situação'] = 'REPROVADO'

    return dicio


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
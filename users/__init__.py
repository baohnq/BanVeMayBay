def encoder(strText):
    rslt = ''
    for i in strText:
        rslt.append(i*2+2)
    return rslt

def decoder(strText):
    rslt = ''
    for i in strText:
        rslt.append(i/2 - 1)
    return rslt

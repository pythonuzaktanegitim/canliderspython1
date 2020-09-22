def Fonk(sayi):
    if not sayi == 0:
        if sayi == 1:
            return sayi
        else:
            return sayi*Fonk(sayi-1)
    else:
        return 1
                
Fonk(8)
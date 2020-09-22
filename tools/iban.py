
class DogrulamaTool():
    def __init__(self,metin):
        self.metin = metin

    def ibanDogrulama(self):
        metin =  self.metin.replace(" ","") 
        if metin.isalnum():
            metin = metin[4:] + metin[:4]
            iban2 = ""
            for kar in metin:
                if not kar.isdigit():
                    iban2 += str(ord(kar)-55)
                else:
                    iban2 += kar
            a = iban2[:9]
            b = str(int(a)%97) +  iban2[9:18]
            c = str(int(b)%97) + iban2[18:]
            sonuc = str(int(c)%97)
            if sonuc == "1":
                return True
            else:
                return False
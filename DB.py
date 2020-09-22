import sqlite3 as sql

class DB():
       
    def __init__(self):
        self.baglan()


    def baglan(self):
        self.db = sql.connect(r"DB\FACEDET.db")
        self.cur = self.db.cursor()

    def PersonelEkleme(self,adi,soyadi,il,ilce):
        try:
            query = """ INSERT INTO PERSONEL (
                                            ADI,
                                            SOYADI,
                                            IL,
                                            ILCE)
                                        VALUES (
                                            '{}',
                                            '{}',
                                            {},
                                            {})
                    """.format(adi,soyadi,il,ilce)
            self.cur.execute(query)
            self.db.commit()
            return True
        except Exception as hata:
            print("hata",hata)
            return False
        finally:
            self.db.close()

    def ekleme(self,yazi="Boş Geldi"):
        try:
            query = " INSERT INTO PYQTDENEME (YAZI) VALUES ('{}')"
            query = query.format(yazi)
            self.cur.execute(query)
            self.db.commit()
            return True
        except:
            return False
        finally:
            self.db.close()

             
    def ilListele(self):
        try:
            self.baglan()
            query =""" SELECT 
                IL_ID,IL_ADI 
                FROM ST_ILLER"""
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as hata:
            liste = []
            liste.append((1,hata))
            return liste
        finally:
            self.db.close()


    def ilceListele(self,ilID = -1):
        try:
            self.baglan()
            query =""" SELECT 
                ILCE_ID,ILCE_ADI 
                FROM ST_ILCELER where IL_ID = {} """.format(ilID)
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as hata:
            liste = []
            liste.append((1,hata))
            return liste
        finally:
            self.db.close()
 


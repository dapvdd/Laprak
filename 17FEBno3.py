class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi 
        
    def luas(self):
        return self.sisi * self.sisi
    
    def keliling(self):
        return 4 * self.sisi
    
sisi = float(input("masukkan panjang sisi = "))
persegi = Persegi(sisi)

print("luas persegi = ",persegi.luas())
print("keliling persegi = ",persegi.keliling())

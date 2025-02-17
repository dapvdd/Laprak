class Mobil:
    def __init__(self, merk, tahun):  # Konstruktor
        self.merk = merk
        self.tahun = tahun

    def info(self):  
        print(f"Mobil {self.merk} keluaran tahun {self.tahun}.")

def main():
    mobil1 = Mobil("Toyota", 2022)
    mobil2 = Mobil("Honda", 2020)

    mobil1.info()
    mobil2.info()
    
if __name__ == "__main__":
    main()

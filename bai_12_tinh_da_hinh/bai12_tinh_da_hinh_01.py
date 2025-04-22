class DongVat:
    def keu(self):
        print("Động vật đang kêu...")

class Meo(DongVat):
    def keu(self):
        print("Meo meo!")

class Cho(DongVat):
    def keu(self):
        print("Gâu gâu!")

# Sử dụng đa hình
def test_keu(dong_vat):
    dong_vat.keu()

# Test
dv1 = Meo()
dv2 = Cho()

test_keu(dv1)  # Kết quả: Meo meo!
test_keu(dv2)  # Kết quả: Gâu gâu!

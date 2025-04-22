'''
@classmethod dùng để đổi thông tin chung toàn class (_ten_cong_ty).

@property.setter dùng để cập nhật thông tin riêng từng object (gia).
'''
class SanPham:
    _ten_cong_ty = "Cửa hàng ABC"

    def __init__(self, ma_sp, ten, gia):
        self.__ma_sp = ma_sp
        self.__ten = ten
        self.__gia = gia  # private

    # Getter cho giá
    @property
    def gia(self):
        return self.__gia

    # Setter cho giá
    @gia.setter
    def gia(self, gia_moi):
        if gia_moi >= 0:
            self.__gia = gia_moi
        else:
            raise ValueError("Giá sản phẩm phải >= 0")

    # Getter tên công ty
    @classmethod
    def lay_ten_cong_ty(cls):
        return cls._ten_cong_ty

    # Setter tên công ty
    @classmethod
    def doi_ten_cong_ty(cls, ten_moi):
        cls._ten_cong_ty = ten_moi

    def hien_thi(self):
        print(f"[{self.__ma_sp}] {self.__ten} - {self.__gia:,.0f} VND (thuộc {self.lay_ten_cong_ty()})")


# Test
if __name__ == "__main__":
    sp1 = SanPham("SP001", "Áo Thun", 120000)
    sp2 = SanPham("SP002", "Quần Jeans", 250000)

    sp1.hien_thi()
    sp2.gia = 275000  # sử dụng setter

    # Đổi tên công ty (áp dụng cho toàn bộ class)
    SanPham.doi_ten_cong_ty("Cửa hàng XYZ")

    sp1.hien_thi()
    sp2.hien_thi()

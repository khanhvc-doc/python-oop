'''
@classmethod: chỉnh sửa hoặc thao tác với class, áp dụng cho tất cả các object của class đó.

@property.setter: thao tác với thuộc tính riêng của từng object,
'''

class CongTy:
    cong_ty = "ABC Corp"

    @classmethod
    def doi_ten_cong_ty(cls, ten_moi):
        cls.cong_ty = ten_moi


    def main():
        print(CongTy.cong_ty)
        CongTy.doi_ten_cong_ty("XYZ Ltd")  # thay đổi cho toàn bộ class
        print(CongTy.cong_ty)


class NhanVien:
    def __init__(self, ho_ten):
        self._ho_ten = ho_ten

    @property
    def ho_ten(self):
        return self._ho_ten

    @ho_ten.setter
    def ho_ten(self, ten_moi):
        self._ho_ten = ten_moi

    def main():
        nv = NhanVien("Nguyen Van A")
        nv.ho_ten = "Nguyen Van B"  # Gọi setter
        print(nv.ho_ten)


# Test
if __name__ == '__main__':
    CongTy.main()
    # NhanVien.main()


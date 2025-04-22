from datetime import datetime

class NhanVien:
    cong_ty = "ABC Corp"  # Thuộc tính lớp

    def __init__(self, ho_ten, nam_sinh):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh

    def tinh_tuoi(self):
        return datetime.now().year - self.nam_sinh

    @staticmethod
    def chao_mung(): 
        # không có self
        print("Chào mừng bạn đến với công ty!")

    @classmethod
    def doi_ten_cong_ty(cls, ten_moi):
        # cls là tên biến, đặt gì cũng được
        # thay giá trị của cong_ty thành tên mới
        cls.cong_ty = ten_moi


# TEST
if __name__ == "__main__":
    nv1 = NhanVien("Nguyen Van A", 1990)
    nv2 = NhanVien("Tran Thi B", 1995)

    # Gọi instance method
    print(nv1.ho_ten, "năm nay", nv1.tinh_tuoi(), "tuổi")

    # Gọi static method
    NhanVien.chao_mung()

    # Gọi class method
    print("Tên công ty hiện tại:", NhanVien.cong_ty)
    NhanVien.doi_ten_cong_ty("XYZ Ltd")
    print("Tên công ty mới:", NhanVien.cong_ty)


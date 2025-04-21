# bai05_nhanvien.py

from bai01_connguoi import ConNguoi
from bai05_interface_thunhap import IThuNhap

class NhanVien(ConNguoi, IThuNhap):
    def __init__(self, ho_ten: str, ngay_sinh: str, gioi_tinh: str, dia_chi: str,
                 ma_nhan_vien: str, luong_co_ban: float):
        super().__init__(ho_ten, ngay_sinh, gioi_tinh, dia_chi)
        self.ma_nhan_vien = ma_nhan_vien
        self.luong_co_ban = luong_co_ban
        # các bạn tự cập nhật nhé

    def __str__(self):
        return (f"{super().__str__()}, Mã NV: {self.ma_nhan_vien}, "
                f"Lương CB: {self.luong_co_ban:,.0f}")

    def hien_thi_thong_tin(self):
        print(self.__str__())

# Demo test 
if __name__ == "__main__":

    print("Không thể tạo đối tượng trực tiếp vì nó chứa phương thức trừu tượng.")
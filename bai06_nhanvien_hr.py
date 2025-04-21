# bai06_nhanvien_hr.py

from bai05_nhanvien import NhanVien

class NhanVienHR(NhanVien):
    def __init__(self, ho_ten: str, ngay_sinh: str, gioi_tinh: str, dia_chi: str, ma_nhan_vien: str, luong_co_ban: float):
        super().__init__(ho_ten, ngay_sinh, gioi_tinh, dia_chi, ma_nhan_vien, luong_co_ban)
        

    def get_thu_nhap(self) -> float:
        """Lương cơ bản"""
        return self.luong_co_ban

    def get_thue(self) -> float:
        """Thuế = 10% thu nhập"""
        return self.get_thu_nhap() * 0.10

    def get_bao_hiem(self) -> float:
        """Bảo hiểm = 8% lương cơ bản"""
        return self.luong_co_ban * 0.08

    def get_phuc_loi(self) -> float:
        """Phúc lợi cố định = 500,000"""
        return 500000

    def hien_thi_chi_tiet(self):
        """Hiển thị thông tin chi tiết bao gồm thu nhập, thuế, BH, phúc lợi"""
        self.hien_thi_thong_tin()
        print(f"Thu nhập:       {self.get_thu_nhap():,.0f} VND")
        print(f"Thuế:           {self.get_thue():,.0f} VND")
        print(f"Bảo hiểm:       {self.get_bao_hiem():,.0f} VND")
        print(f"Phúc lợi:       {self.get_phuc_loi():,.0f} VND")
        thuc_nhan = self.get_thu_nhap() - self.get_thue() - self.get_bao_hiem() + self.get_phuc_loi()
        print(f"Thực nhận:      {thuc_nhan:,.0f} VND")

# Test hoặc cũng có thể tạo file py riêng để test
if __name__ == "__main__":
    print("== Demo NhanVienHR ==")
    nv = NhanVienHR("Nguyen Thi Hoa", "10/10/2011", "Nữ", "Thu Duc - HCM", "HR001", 10000000)
    nv.hien_thi_chi_tiet()
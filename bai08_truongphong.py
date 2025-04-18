# bai08_truongphong.py

from bai05_nhanvien import NhanVien

class TruongPhong(NhanVien):
    def __init__(
        self,
        ho_ten: str,
        tuoi: int,
        gioi_tinh: str,
        ma_nhan_vien: str,
        luong_co_ban: float,
        phu_cap_trach_nhiem: float,
        he_so_chuc_vu: float,
        so_nam_cong_tac: int
    ):
        super().__init__(ho_ten, tuoi, gioi_tinh, ma_nhan_vien, luong_co_ban)
        self.phu_cap_trach_nhiem = phu_cap_trach_nhiem
        self.he_so_chuc_vu = he_so_chuc_vu
        self.so_nam_cong_tac = so_nam_cong_tac

    def get_thu_nhap(self) -> float:
        return self.luong_co_ban * self.he_so_chuc_vu + self.phu_cap_trach_nhiem

    def get_thue(self) -> float:
        return self.get_thu_nhap() * 0.1

    def get_bao_hiem(self) -> float:
        return self.luong_co_ban * 0.08

    def get_phuc_loi(self) -> float:
        return 1_000_000 + self.so_nam_cong_tac * 100_000

    def hien_thi_chi_tiet(self):
        self.hien_thi_thong_tin()
        print(f"Hệ số chức vụ:       {self.he_so_chuc_vu}")
        print(f"Phụ cấp trách nhiệm:  {self.phu_cap_trach_nhiem:,.0f} VND")
        print(f"Năm công tác:         {self.so_nam_cong_tac}")
        print(f"Thu nhập:             {self.get_thu_nhap():,.0f} VND")
        print(f"Thuế:                 {self.get_thue():,.0f} VND")
        print(f"Bảo hiểm:             {self.get_bao_hiem():,.0f} VND")
        print(f"Phúc lợi:             {self.get_phuc_loi():,.0f} VND")
        thuc_nhan = self.get_thu_nhap() - self.get_thue() - self.get_bao_hiem() + self.get_phuc_loi()
        print(f"Thực nhận:            {thuc_nhan:,.0f} VND")


# Test

if __name__ == '__main__':
    print("== Demo TruongPhong ==")
    tp = TruongPhong(
        ho_ten="Tony Tèo",
        tuoi=45,
        gioi_tinh="Nam",
        ma_nhan_vien="TP01",
        luong_co_ban=15000000,
        phu_cap_trach_nhiem=3000000,
        he_so_chuc_vu=1.6,
        so_nam_cong_tac=10
    )
    tp.hien_thi_chi_tiet()
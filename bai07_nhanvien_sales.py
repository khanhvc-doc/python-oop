# bai07_nhanvien_sales.py

from bai05_nhanvien import NhanVien

class NhanVienSales(NhanVien):
    def __init__( 
        self, 
        ho_ten: str,
        tuoi: int,
        gioi_tinh: str,
        ma_nhan_vien: str,
        luong_co_ban: float,
        doanh_so: float,
        hoa_hong: float  # ví dụ: 5% = 0.05
    ):
        super().__init__(ho_ten, tuoi, gioi_tinh, ma_nhan_vien, luong_co_ban)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def get_thu_nhap(self) -> float:
        return self.luong_co_ban + self.doanh_so * self.hoa_hong

    def get_thue(self) -> float:
        return self.get_thu_nhap() * 0.10

    def get_bao_hiem(self) -> float:
        return self.luong_co_ban * 0.08

    def get_phuc_loi(self) -> float:
        return 1_000_000  # Sales có thể được phúc lợi cao hơn

    def hien_thi_chi_tiet(self):
        self.hien_thi_thong_tin()
        print(f"Doanh số:       {self.doanh_so:,.0f} VND")
        print(f"Hoa hồng:       {self.hoa_hong*100:.1f} %")
        print(f"Thu nhập:       {self.get_thu_nhap():,.0f} VND")
        print(f"Thuế:           {self.get_thue():,.0f} VND")
        print(f"Bảo hiểm:       {self.get_bao_hiem():,.0f} VND")
        print(f"Phúc lợi:       {self.get_phuc_loi():,.0f} VND")
        thuc_nhan = self.get_thu_nhap() - self.get_thue() - self.get_bao_hiem() + self.get_phuc_loi()
        print(f"Thực nhận:      {thuc_nhan:,.0f} VND")


# test 
if __name__ == '__main__':
    nv = NhanVienSales(
        ho_ten='Van Cong Khanh',
        tuoi= 30,
        gioi_tinh= 'Nam',
        ma_nhan_vien= 'NVSales01',
        luong_co_ban= 800000,
        doanh_so= 10000000,
        hoa_hong=0.05

    )
    nv.hien_thi_chi_tiet()
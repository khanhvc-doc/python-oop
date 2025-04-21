# bai03_sinhvien_it.py

from bai02_sinhvien import SinhVien

class SinhVienIT(SinhVien):
    def __init__(self, ho_ten: str, tuoi: int, gioi_tinh: str, ma_sinh_vien: str,
                 diem_A: float, diem_B: float, diem_C: float):
        super().__init__(ho_ten, tuoi, gioi_tinh, ma_sinh_vien)
        self.diem_A = diem_A
        self.diem_B = diem_B
        self.diem_C = diem_C

    def get_diem(self) -> float:
        return self.diem_A * 0.4 + self.diem_B * 0.35 + self.diem_C * 0.25

    def xep_loai(self) -> str:
        diem_tb = self.get_diem()
        if diem_tb >= 8.5:
            return "Giỏi"
        elif diem_tb >= 7.0:
            return "Khá"
        elif diem_tb >= 5.5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return (f"{super().__str__()}, Điểm A: {self.diem_A}, "
                f"Điểm B: {self.diem_B}, Điểm C: {self.diem_C}, "
                f"Điểm TB: {self.get_diem():.2f}, Xếp loại: {self.xep_loai()}")

    def hien_thi_thong_tin(self):
        print(self.__str__())

# Demo test khi chạy trực tiếp
if __name__ == "__main__":
    sv_it = SinhVienIT("Trần Văn B", "10/10/2000", "Nam", "IT001", 8.0, 7.5, 9.0)
    sv_it.hien_thi_thong_tin()

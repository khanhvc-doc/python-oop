# bai04_sinhvien_kd.py

from bai02_sinhvien import SinhVien

class SinhVienKD(SinhVien):
    def __init__(self, ho_ten: str, tuoi: int, gioi_tinh: str, ma_sinh_vien: str,
                 diem_X: float, diem_Y: float, diem_Z: float):
        super().__init__(ho_ten, tuoi, gioi_tinh, ma_sinh_vien)
        self.diem_X = diem_X
        self.diem_Y = diem_Y
        self.diem_Z = diem_Z

    def get_diem(self) -> float:
        return self.diem_X * 0.2 + self.diem_Y * 0.3 + self.diem_Z * 0.5

    def xep_loai(self) -> str:
        diem_tb = self.get_diem()
        # cố tình yêu cầu cao hơn tí
        if diem_tb >= 8.5:
            return "Giỏi"
        elif diem_tb >= 7.5:
            return "Khá"
        elif diem_tb >= 6.0:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return (f"{super().__str__()}, Điểm X: {self.diem_X}, "
                f"Điểm Y: {self.diem_Y}, Điểm Z: {self.diem_Z}, "
                f"Điểm TB: {self.get_diem():.2f}, Xếp loại: {self.xep_loai()}")

    def hien_thi_thong_tin(self):
        print(self.__str__())

# Demo test
if __name__ == "__main__":
    sv_kd = SinhVienKD("Nguyễn Thị C", 21, "Nữ", "KD001", 7.0, 7.5, 9.0)
    sv_kd.hien_thi_thong_tin()

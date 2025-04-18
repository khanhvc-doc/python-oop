# bai02_sinhvien.py

from abc import ABC, abstractmethod
from bai01_connguoi_Update import ConNguoi

class SinhVien(ConNguoi, ABC):
    def __init__(self, ho_ten: str, tuoi: int, gioi_tinh: str, ma_sinh_vien: str):
        super().__init__(ho_ten, tuoi, gioi_tinh)
        self.ma_sinh_vien = ma_sinh_vien

    def __str__(self):
        return f"{super().__str__()}, Mã SV: {self.ma_sinh_vien}"

    def hien_thi_thong_tin(self):
        print(self.__str__())

    @abstractmethod
    def get_diem(self) -> float:
        #  buộc các lớp con phải override
        pass

    @abstractmethod
    def xep_loai(self) -> str:
        #  buộc các lớp con phải override
        pass

# Demo test khi chạy trực tiếp
if __name__ == "__main__":
    # Không thể tạo instance SinhVien vì là lớp trừu tượng
    print("Không thể tạo đối tượng từ lớp SinhVien trực tiếp vì nó chứa phương thức trừu tượng.")
